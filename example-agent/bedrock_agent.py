#!/usr/bin/env python3
"""
AWS Bedrock Agent for Documentation Assistance
Exposed as MCP tools via FastMCP to mcp-orch
"""

import json
import os
import uuid
from typing import Dict, Any, Optional, List
from datetime import datetime

import boto3
from botocore.exceptions import ClientError
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MCP Server Configuration
mcp = FastMCP("sample-documentation-agent")

# AWS Bedrock Agent Configuration
class BedrockAgentConfig:
    def __init__(self):
        self.region = os.getenv('AWS_REGION', 'us-east-1')
        self.agent_id = os.getenv('BEDROCK_AGENT_ID')
        self.agent_alias_id = os.getenv('BEDROCK_AGENT_ALIAS_ID', 'TSTALIASID')
        self.knowledge_base_id = os.getenv('BEDROCK_KNOWLEDGE_BASE_ID')
        self.session_id = str(uuid.uuid4())
        
        # Initialize Bedrock Agent Runtime client
        try:
            self.client = boto3.client(
                'bedrock-agent-runtime',
                region_name=self.region
            )
        except Exception as e:
            print(f"Error initializing Bedrock Agent client: {e}")
            self.client = None

# Global configuration
config = BedrockAgentConfig()

# Session storage (in production, use a proper database)
sessions: Dict[str, Dict[str, Any]] = {}

# Pydantic models for request/response
class AgentStartRequest(BaseModel):
    session_id: Optional[str] = Field(None, description="Optional custom session ID")
    user_id: Optional[str] = Field(None, description="User identifier")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")

class AgentStartResponse(BaseModel):
    session_id: str = Field(..., description="Session identifier")
    status: str = Field(..., description="Status of agent start")
    message: str = Field(..., description="Initial response from the agent")

class AgentSendRequest(BaseModel):
    session_id: str = Field(..., description="Session identifier")
    message: str = Field(..., description="User message to send to the agent")
    user_id: Optional[str] = Field(None, description="User identifier")

class AgentSendResponse(BaseModel):
    session_id: str = Field(..., description="Session identifier")
    response: str = Field(..., description="Agent's response")
    status: str = Field(..., description="Status of the message processing")
    citations: Optional[List[Dict[str, Any]]] = Field(None, description="Knowledge base citations")

class AgentFinalizeRequest(BaseModel):
    session_id: str = Field(..., description="Session identifier to finalize")

class AgentFinalizeResponse(BaseModel):
    session_id: str = Field(..., description="Finalized session identifier")
    status: str = Field(..., description="Status of session finalization")
    summary: Optional[str] = Field(None, description="Summary of the session")

def call_bedrock_agent(session_id: str, message: str, user_id: str = None) -> Dict[str, Any]:
    """Call AWS Bedrock Agent"""
    if not config.client:
        return {
            "response": "Error: Bedrock Agent client not initialized. Please check AWS configuration.",
            "citations": None
        }
    
    if not config.agent_id:
        return {
            "response": "Error: Bedrock Agent ID not configured. Please set BEDROCK_AGENT_ID environment variable.",
            "citations": None
        }
    
    try:
        # Prepare the request
        request_params = {
            "agentId": config.agent_id,
            "agentAliasId": config.agent_alias_id,
            "sessionId": session_id,
            "inputText": message
        }
        
        if user_id:
            request_params["sessionState"] = {
                "sessionAttributes": {
                    "userId": user_id
                }
            }
        
        # Call Bedrock Agent
        response = config.client.invoke_agent(**request_params)
        
        # Process the streaming response
        response_text = ""
        citations = []
        
        for event in response['completion']:
            if 'chunk' in event:
                chunk = event['chunk']
                if 'bytes' in chunk:
                    response_text += chunk['bytes'].decode('utf-8')
            
            if 'trace' in event:
                trace = event['trace']
                if 'orchestrationTrace' in trace:
                    orchestration = trace['orchestrationTrace']
                    if 'invocationInput' in orchestration:
                        invocation = orchestration['invocationInput']
                        if 'actionGroupInvocationInput' in invocation:
                            action_group = invocation['actionGroupInvocationInput']
                            if 'function' in action_group:
                                function = action_group['function']
                                if 'response' in function:
                                    response_data = function['response']
                                    if 'actionGroupInvocationOutput' in response_data:
                                        output = response_data['actionGroupInvocationOutput']
                                        if 'text' in output:
                                            response_text += output['text']
        
        # Extract citations if available
        if 'citations' in response:
            citations = response['citations']
        
        return {
            "response": response_text.strip(),
            "citations": citations
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        return {
            "response": f"Error calling Bedrock Agent: {error_code} - {error_message}",
            "citations": None
        }
    except Exception as e:
        return {
            "response": f"Unexpected error: {str(e)}",
            "citations": None
        }

@mcp.tool()
def agent_start(request: AgentStartRequest) -> AgentStartResponse:
    """Start a new Bedrock Agent session"""
    session_id = request.session_id or str(uuid.uuid4())
    
    # Store session
    sessions[session_id] = {
        "created_at": datetime.now().isoformat(),
        "user_id": request.user_id,
        "context": request.context or {},
        "status": "active"
    }
    
    # Initial message to start the conversation
    initial_message = "Hello! I'm your documentation assistant powered by AWS Bedrock. How can I help you with documentation today?"
    
    # Get initial response from Bedrock Agent
    result = call_bedrock_agent(session_id, initial_message, request.user_id)
    
    return AgentStartResponse(
        session_id=session_id,
        status="started",
        message=result["response"]
    )

@mcp.tool()
def agent_send(request: AgentSendRequest) -> AgentSendResponse:
    """Send a message to the Bedrock Agent"""
    if request.session_id not in sessions:
        return AgentSendResponse(
            session_id=request.session_id,
            response="Error: Session not found",
            status="error",
            citations=None
        )
    
    session = sessions[request.session_id]
    
    # Get response from Bedrock Agent
    result = call_bedrock_agent(request.session_id, request.message, request.user_id)
    
    # Update session
    session["updated_at"] = datetime.now().isoformat()
    session["last_message"] = request.message
    session["last_response"] = result["response"]
    
    return AgentSendResponse(
        session_id=request.session_id,
        response=result["response"],
        status="success",
        citations=result["citations"]
    )

@mcp.tool()
def agent_finalize(request: AgentFinalizeRequest) -> AgentFinalizeResponse:
    """Finalize a Bedrock Agent session"""
    if request.session_id not in sessions:
        return AgentFinalizeResponse(
            session_id=request.session_id,
            status="error",
            summary="Error: Session not found"
        )
    
    session = sessions[request.session_id]
    
    # Generate summary using Bedrock Agent
    summary_message = "Please provide a brief summary of our conversation, highlighting the main topics discussed and any key recommendations."
    result = call_bedrock_agent(request.session_id, summary_message, session.get("user_id"))
    
    # Mark session as finalized
    session["finalized_at"] = datetime.now().isoformat()
    session["status"] = "finalized"
    session["summary"] = result["response"]
    
    return AgentFinalizeResponse(
        session_id=request.session_id,
        status="finalized",
        summary=result["response"]
    )

@mcp.tool()
def get_session_info(session_id: str) -> Dict[str, Any]:
    """Get information about a specific session"""
    if session_id not in sessions:
        return {"error": "Session not found"}
    
    session = sessions[session_id]
    return {
        "session_id": session_id,
        "created_at": session.get("created_at"),
        "updated_at": session.get("updated_at"),
        "finalized_at": session.get("finalized_at"),
        "status": session.get("status", "active"),
        "user_id": session.get("user_id"),
        "context": session.get("context"),
        "summary": session.get("summary")
    }

@mcp.tool()
def list_sessions() -> Dict[str, Any]:
    """List all active sessions"""
    return {
        "sessions": [
            {
                "session_id": session_id,
                "created_at": session["created_at"],
                "status": session.get("status", "active"),
                "user_id": session.get("user_id")
            }
            for session_id, session in sessions.items()
        ],
        "total": len(sessions)
    }

@mcp.tool()
def get_agent_info() -> Dict[str, Any]:
    """Get information about the Bedrock Agent configuration"""
    return {
        "agent_id": config.agent_id,
        "agent_alias_id": config.agent_alias_id,
        "knowledge_base_id": config.knowledge_base_id,
        "region": config.region,
        "status": "configured" if config.client and config.agent_id else "not_configured"
    }

if __name__ == "__main__":
    print("Starting AWS Bedrock Agent MCP Server...")
    print("Make sure to configure AWS credentials and Bedrock Agent ID")
    print("Server name: sample-documentation-agent")
    print("Available tools:")
    print("- agent_start: Start a new agent session")
    print("- agent_send: Send a message to the agent")
    print("- agent_finalize: Finalize an agent session")
    print("- get_session_info: Get session details")
    print("- list_sessions: List all sessions")
    print("- get_agent_info: Get agent configuration info")
    
    if not config.agent_id:
        print("\nWARNING: BEDROCK_AGENT_ID not configured!")
        print("Please set the BEDROCK_AGENT_ID environment variable with your Bedrock Agent ID")
    
    # Run the MCP server
    mcp.run()

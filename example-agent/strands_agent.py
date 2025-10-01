#!/usr/bin/env python3
"""
Documentation Assistant using AWS Strands Agents
Exposed as MCP tools via FastMCP to mcp-orch
"""

import json
import os
import uuid
from typing import Dict, Any, Optional, List
from datetime import datetime

from strands_agents import Agent, BedrockProvider
from strands_agents.tools import Tool
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MCP Server Configuration
mcp = FastMCP("sample-documentation-agent")

# Strands Agent Configuration
class StrandsAgentConfig:
    def __init__(self):
        self.region = os.getenv('AWS_REGION', 'us-east-1')
        self.model_id = os.getenv('BEDROCK_MODEL_ID', 'anthropic.claude-3-5-sonnet-20241022-v2:0')
        
        # Initialize Bedrock provider
        try:
            self.provider = BedrockProvider(
                region=self.region,
                model_id=self.model_id
            )
        except Exception as e:
            print(f"Error initializing Bedrock provider: {e}")
            self.provider = None

# Global configuration
config = StrandsAgentConfig()

# Session storage (in production, use a proper database)
sessions: Dict[str, Dict[str, Any]] = {}

# Pydantic models for request/response
class AgentStartRequest(BaseModel):
    session_id: Optional[str] = Field(None, description="Optional custom session ID")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")
    headers: Optional[Dict[str, str]] = Field(None, description="Headers from mcp-orch")

class AgentStartResponse(BaseModel):
    session_id: str = Field(..., description="Session identifier")
    status: str = Field(..., description="Status of agent start")
    message: str = Field(..., description="Initial response from the agent")

class AgentSendRequest(BaseModel):
    session_id: str = Field(..., description="Session identifier")
    message: str = Field(..., description="User message to send to the agent")
    headers: Optional[Dict[str, str]] = Field(None, description="Headers from mcp-orch")

class AgentSendResponse(BaseModel):
    session_id: str = Field(..., description="Session identifier")
    response: str = Field(..., description="Agent's response")
    status: str = Field(..., description="Status of the message processing")
    tools_used: Optional[List[str]] = Field(None, description="Tools used by the agent")

class AgentFinalizeRequest(BaseModel):
    session_id: str = Field(..., description="Session identifier to finalize")
    headers: Optional[Dict[str, str]] = Field(None, description="Headers from mcp-orch")

class AgentFinalizeResponse(BaseModel):
    session_id: str = Field(..., description="Finalized session identifier")
    status: str = Field(..., description="Status of session finalization")
    summary: Optional[str] = Field(None, description="Summary of the session")

# Documentation-specific tools
@Tool
def search_documentation(query: str) -> str:
    """Search through documentation for relevant information"""
    # In a real implementation, this would search your knowledge base
    return f"Found documentation related to: {query}. This is a placeholder response."

@Tool
def generate_documentation_outline(topic: str) -> str:
    """Generate a structured outline for documentation on a given topic"""
    return f"Documentation outline for '{topic}':\n1. Introduction\n2. Prerequisites\n3. Getting Started\n4. API Reference\n5. Examples\n6. Troubleshooting"

@Tool
def review_documentation(content: str) -> str:
    """Review documentation content for clarity, completeness, and best practices"""
    return f"Documentation review for content: {content[:100]}...\n\nSuggestions:\n- Consider adding more examples\n- Ensure technical terms are defined\n- Check for consistent formatting"

@Tool
def suggest_improvements(content: str) -> str:
    """Suggest specific improvements for documentation content"""
    return f"Improvement suggestions for: {content[:100]}...\n\n1. Add code examples\n2. Include error handling scenarios\n3. Provide troubleshooting section"

# Create Strands Agent
def create_documentation_agent() -> Agent:
    """Create a Strands Agent configured for documentation assistance"""
    if not config.provider:
        raise Exception("Bedrock provider not initialized")
    
    agent = Agent(
        provider=config.provider,
        system_prompt="""You are a helpful documentation assistant powered by AWS Strands Agents. 
        Your role is to help users with:
        1. Understanding technical concepts
        2. Creating clear, comprehensive documentation
        3. Reviewing and improving existing documentation
        4. Suggesting best practices for technical writing
        5. Organizing information effectively
        
        You have access to several tools to help with documentation tasks.
        Be concise, accurate, and helpful. If you don't know something, say so clearly.""",
        tools=[
            search_documentation,
            generate_documentation_outline,
            review_documentation,
            suggest_improvements
        ]
    )
    
    return agent

def get_user_id_from_headers(headers: Optional[Dict[str, str]]) -> Optional[str]:
    """Extract user ID from forwarded headers"""
    if not headers:
        return None
    return headers.get("X-Subject-Id")

def get_tenant_id_from_headers(headers: Optional[Dict[str, str]]) -> Optional[str]:
    """Extract tenant ID from forwarded headers"""
    if not headers:
        return None
    return headers.get("X-Tenant-Id")

def get_client_id_from_headers(headers: Optional[Dict[str, str]]) -> Optional[str]:
    """Extract client ID from forwarded headers"""
    if not headers:
        return None
    return headers.get("X-Client-Id")

@mcp.tool()
def agent_start(request: AgentStartRequest) -> AgentStartResponse:
    """Start a new Strands Agent session"""
    session_id = request.session_id or str(uuid.uuid4())
    
    try:
        # Create agent for this session
        agent = create_documentation_agent()
        
        # Get user ID from headers
        user_id = get_user_id_from_headers(request.headers)
        tenant_id = get_tenant_id_from_headers(request.headers)
        client_id = get_client_id_from_headers(request.headers)
        
        # Store session with agent
        sessions[session_id] = {
            "created_at": datetime.now().isoformat(),
            "user_id": user_id,
            "tenant_id": tenant_id,
            "client_id": client_id,
            "context": request.context or {},
            "status": "active",
            "agent": agent
        }
        
        # Initial message
        initial_message = "Hello! I'm your documentation assistant powered by AWS Strands Agents. I can help you with creating, reviewing, and improving technical documentation. What would you like help with today?"
        
        # Get initial response from agent
        response = agent.run(initial_message)
        
        return AgentStartResponse(
            session_id=session_id,
            status="started",
            message=response.content
        )
        
    except Exception as e:
        return AgentStartResponse(
            session_id=session_id,
            status="error",
            message=f"Error starting agent: {str(e)}"
        )

@mcp.tool()
def agent_send(request: AgentSendRequest) -> AgentSendResponse:
    """Send a message to the Strands Agent"""
    if request.session_id not in sessions:
        return AgentSendResponse(
            session_id=request.session_id,
            response="Error: Session not found",
            status="error",
            tools_used=None
        )
    
    try:
        session = sessions[request.session_id]
        agent = session["agent"]
        
        # Send message to agent
        response = agent.run(request.message)
        
        # Update session
        session["updated_at"] = datetime.now().isoformat()
        session["last_message"] = request.message
        session["last_response"] = response.content
        
        # Extract tools used (if available)
        tools_used = []
        if hasattr(response, 'tool_calls') and response.tool_calls:
            tools_used = [call.function.name for call in response.tool_calls]
        
        return AgentSendResponse(
            session_id=request.session_id,
            response=response.content,
            status="success",
            tools_used=tools_used
        )
        
    except Exception as e:
        return AgentSendResponse(
            session_id=request.session_id,
            response=f"Error processing message: {str(e)}",
            status="error",
            tools_used=None
        )

@mcp.tool()
def agent_finalize(request: AgentFinalizeRequest) -> AgentFinalizeResponse:
    """Finalize a Strands Agent session"""
    if request.session_id not in sessions:
        return AgentFinalizeResponse(
            session_id=request.session_id,
            status="error",
            summary="Error: Session not found"
        )
    
    try:
        session = sessions[request.session_id]
        agent = session["agent"]
        
        # Generate summary using agent
        summary_message = "Please provide a brief summary of our conversation, highlighting the main topics discussed and any key recommendations for documentation."
        response = agent.run(summary_message)
        
        # Mark session as finalized
        session["finalized_at"] = datetime.now().isoformat()
        session["status"] = "finalized"
        session["summary"] = response.content
        
        return AgentFinalizeResponse(
            session_id=request.session_id,
            status="finalized",
            summary=response.content
        )
        
    except Exception as e:
        return AgentFinalizeResponse(
            session_id=request.session_id,
            status="error",
            summary=f"Error finalizing session: {str(e)}"
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
    """Get information about the Strands Agent configuration"""
    return {
        "framework": "AWS Strands Agents",
        "model_id": config.model_id,
        "region": config.region,
        "status": "configured" if config.provider else "not_configured",
        "tools_available": [
            "search_documentation",
            "generate_documentation_outline", 
            "review_documentation",
            "suggest_improvements"
        ]
    }

if __name__ == "__main__":
    print("Starting AWS Strands Agents MCP Server...")
    print("Make sure to configure AWS credentials")
    print("Server name: sample-documentation-agent")
    print("Available tools:")
    print("- agent_start: Start a new agent session")
    print("- agent_send: Send a message to the agent")
    print("- agent_finalize: Finalize an agent session")
    print("- get_session_info: Get session details")
    print("- list_sessions: List all sessions")
    print("- get_agent_info: Get agent configuration info")
    
    if not config.provider:
        print("\nWARNING: Bedrock provider not initialized!")
        print("Please check your AWS credentials and region configuration")
    
    # Run the MCP server
    mcp.run()

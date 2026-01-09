# AWS Strands Agents Documentation Assistant

A conversational documentation assistant using [AWS Strands Agents](https://strandsagents.com/latest/), exposed as MCP tools via FastMCP.
This is a Olympus Seer Agent adhering to Olympus Seer MCP Orchestration contract.

## Features

- **AWS Strands Agents Framework**: Production-ready AI agent framework from AWS
- **Model & Provider Agnostic**: Works with any LLM provider (Bedrock, OpenAI, Anthropic, etc.)
- **Built-in Tool Support**: Native tools for documentation assistance
- **Session Management**: Start, send messages, and finalize agent sessions
- **MCP Tools**: Exposed as tools for mcp-orch integration
- **Documentation Focus**: Specialized for helping with technical documentation

## Available Tools

1. **agent_start**: Start a new Strands Agent session
2. **agent_send**: Send a message to the Strands Agent
3. **agent_finalize**: Finalize an agent session with summary
4. **get_session_info**: Get details about a specific session
5. **list_sessions**: List all active sessions
6. **get_agent_info**: Get Strands Agent configuration information

## Built-in Documentation Tools

The agent includes specialized tools for documentation assistance:
- **search_documentation**: Search through documentation for relevant information
- **generate_documentation_outline**: Generate structured outlines for documentation
- **review_documentation**: Review content for clarity and completeness
- **suggest_improvements**: Suggest specific improvements for documentation

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure AWS Credentials

Copy the example environment file and fill in your AWS credentials:

```bash
cp env.example .env
```

Edit `.env` with your AWS credentials:

```bash
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_SESSION_TOKEN=your_session_token  # Optional, for temporary credentials

# Strands Agents Configuration
BEDROCK_MODEL_ID=anthropic.claude-3-5-sonnet-20241022-v2:0
```

### 3. Strands Agents Benefits

[Strands Agents](https://strandsagents.com/latest/) provides several advantages:

- **Production-Ready**: Built by AWS for enterprise use
- **Model Agnostic**: Switch between providers without code changes
- **Native AWS Integration**: Works seamlessly with Bedrock, Lambda, EKS, etc.
- **Built-in Security**: Guardrails and safety features
- **Observability**: Built-in metrics, traces, and logs
- **MCP Integration**: Native support for Model Context Protocol

### 4. Run the Agent

```bash
python strands_agent.py
```

## Tool Specifications for MCP-Orch

### agent_start
- **Input**: `session_id` (optional), `context` (optional), `headers` (from mcp-orch)
- **Output**: `session_id`, `status`, `message`
- **Description**: Starts a new Strands Agent session
- **Note**: User ID is automatically extracted from `X-Subject-Id` header

### agent_send
- **Input**: `session_id`, `message`, `headers` (from mcp-orch)
- **Output**: `session_id`, `response`, `status`, `tools_used` (optional)
- **Description**: Sends a message to the Strands Agent
- **Note**: User context is maintained from session start

### agent_finalize
- **Input**: `session_id`, `headers` (from mcp-orch)
- **Output**: `session_id`, `status`, `summary`
- **Description**: Finalizes an agent session and provides a summary

## Olympus Seer MCP Orchestration Integration

This agent is designed to be registered with mcp-orch as:

- **Server Name**: `sample-documentation-agent`
- **Namespace**: `documentation`
- **Interface**: HTTP(S)
- **Tools**: All conversation management tools

## Example Usage

1. **Start an agent session**:
   ```json
   {
     "tool": "agent_start",
     "input": {
       "context": {
         "project": "microservices-api",
         "domain": "documentation"
       },
       "headers": {
         "X-Subject-Id": "user-123",
         "X-Tenant-Id": "tenant-456",
         "X-Client-Id": "client-app"
       }
     }
   }
   ```

2. **Send a message to the agent**:
   ```json
   {
     "tool": "agent_send",
     "input": {
       "session_id": "uuid-here",
       "message": "What are the key sections I should include in API documentation?",
       "headers": {
         "X-Subject-Id": "user-123",
         "X-Tenant-Id": "tenant-456"
       }
     }
   }
   ```

3. **Finalize agent session**:
   ```json
   {
     "tool": "agent_finalize",
     "input": {
       "session_id": "uuid-here",
       "headers": {
         "X-Subject-Id": "user-123"
       }
     }
   }
   ```

## Configuration

The agent can be configured via environment variables:

- `AWS_REGION`: AWS region (default: us-east-1)
- `BEDROCK_MODEL_ID`: Bedrock model ID (default: Claude 3.5 Sonnet)
- **Provider Support**: Strands Agents supports multiple providers:
  - Amazon Bedrock
  - OpenAI
  - Anthropic
  - LiteLLM
  - Ollama
  - And more

## Error Handling

The agent includes comprehensive error handling for:
- AWS Bedrock API errors
- Invalid session IDs
- Missing AWS credentials
- Network connectivity issues

## Notes

- Sessions are stored in memory (use a database for production)
- AWS Bedrock requires appropriate IAM permissions
- Strands Agents provides built-in observability and monitoring
- The framework handles tool orchestration and agent reasoning automatically
- Native MCP integration for seamless tool management

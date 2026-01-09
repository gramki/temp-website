#!/bin/bash

# AWS Strands Agents Runner
# This script helps run the MCP agent with proper environment setup

echo "Starting AWS Strands Agents MCP Server..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Warning: .env file not found. Please copy env.example to .env and configure AWS credentials."
    echo "cp env.example .env"
    echo "Then edit .env with your AWS credentials."
    exit 1
fi

# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Check if AWS credentials are configured
if [ -z "$AWS_ACCESS_KEY_ID" ] || [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
    echo "Error: AWS credentials not configured in .env file"
    echo "Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY"
    exit 1
fi

# Check if AWS region is set
if [ -z "$AWS_REGION" ]; then
    echo "Warning: AWS_REGION not set, using default us-east-1"
    export AWS_REGION=us-east-1
fi

echo "Configuration:"
echo "  AWS Region: ${AWS_REGION}"
echo "  Model ID: ${BEDROCK_MODEL_ID:-anthropic.claude-3-5-sonnet-20241022-v2:0}"
echo "  Framework: AWS Strands Agents"
echo "  Server: sample-documentation-agent"
echo ""

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting MCP server..."
python strands_agent.py

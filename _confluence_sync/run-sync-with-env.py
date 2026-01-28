#!/usr/bin/env python3
"""Wrapper script to load .env file and run sync-to-confluence.py"""
import os
import sys
from pathlib import Path

# Load .env file from data directory
data_dir = Path(__file__).parent / 'data'
env_file = data_dir / '.env'
if env_file.exists():
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and value and key not in os.environ:
                    os.environ[key] = value
    print(f"✓ Loaded environment variables from {env_file}")
else:
    print(f"⚠ Warning: .env file not found at {env_file}")

# Now run the sync script directly
scripts_dir = Path(__file__).parent / 'scripts'
sync_script = scripts_dir / 'sync-to-confluence.py'

# Change to scripts directory and execute
os.chdir(scripts_dir)
sys.path.insert(0, str(scripts_dir))

# Execute the sync script
with open(sync_script, 'r') as f:
    code = compile(f.read(), str(sync_script), 'exec')
    exec(code, {'__name__': '__main__', '__file__': str(sync_script)})

#!/usr/bin/env python3
"""Wrapper script to load .env file and run sync-to-confluence.py.
Uses scripts/venv when present so sync runs with the same deps (including mmdc for Mermaid).
"""
import os
import sys
from pathlib import Path

# Prefer scripts/venv so sync uses requirements.txt (including mmdc)
_scripts_dir = Path(__file__).resolve().parent / 'scripts'
_venv_python = _scripts_dir / 'venv' / 'bin' / 'python'
if _venv_python.exists() and sys.executable != str(_venv_python):
    os.execv(str(_venv_python), [str(_venv_python), __file__] + sys.argv[1:])

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

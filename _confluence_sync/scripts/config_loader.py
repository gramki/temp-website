#!/usr/bin/env python3
"""
Configuration loader for destination-based Confluence sync.

Loads and validates destination configurations from YAML files.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
import yaml


class ConfigError(Exception):
    """Configuration error."""
    pass


def load_destination_config(config_path: Optional[Path] = None, data_dir: Optional[Path] = None) -> Dict[str, Any]:
    """
    Load destination configuration from YAML file.
    
    Args:
        config_path: Path to config file. If None, looks for confluence-destinations.yaml in data directory.
        data_dir: Optional explicit data directory path
        
    Returns:
        Configuration dictionary
        
    Raises:
        ConfigError: If config file is invalid or missing
    """
    if config_path is None:
        # Look for config in data directory
        from sync_state import get_data_dir
        data_directory = get_data_dir(data_dir)
        config_path = data_directory / 'confluence-destinations.yaml'
        
        # Fallback: check old location (repo root) for migration
        if not config_path.exists():
            script_dir = Path(__file__).parent
            repo_root = script_dir.parent
            old_config_path = repo_root / 'confluence-destinations.yaml'
            if old_config_path.exists():
                # Migrate config to data directory
                data_directory.mkdir(parents=True, exist_ok=True)
                import shutil
                shutil.copy2(old_config_path, config_path)
                print(f"  ✓ Migrated config file to {config_path}")
    
    config_path = Path(config_path).resolve()
    
    if not config_path.exists():
        raise ConfigError(
            f"Configuration file not found: {config_path}\n"
            f"Create a confluence-destinations.yaml file in your repository root."
        )
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ConfigError(f"Invalid YAML in config file: {e}")
    except Exception as e:
        raise ConfigError(f"Error reading config file: {e}")
    
    if not isinstance(config, dict):
        raise ConfigError("Config file must contain a YAML dictionary")
    
    if 'destinations' not in config:
        raise ConfigError("Config file must contain a 'destinations' key")
    
    if not isinstance(config['destinations'], list):
        raise ConfigError("'destinations' must be a list")
    
    if len(config['destinations']) == 0:
        raise ConfigError("At least one destination must be configured")
    
    # Validate each destination (use actual repo root, not config path parent)
    repo_root = get_repo_root()
    for idx, dest in enumerate(config['destinations']):
        try:
            validate_destination_config(dest, repo_root)
        except ConfigError as e:
            raise ConfigError(f"Destination {idx + 1} is invalid: {e}")
    
    return config


def get_destination(config: Dict[str, Any], destination_id: str) -> Dict[str, Any]:
    """
    Get a specific destination configuration by ID.
    
    Args:
        config: Configuration dictionary
        destination_id: Destination ID to retrieve
        
    Returns:
        Destination configuration dictionary
        
    Raises:
        ConfigError: If destination ID not found
    """
    for dest in config.get('destinations', []):
        if dest.get('id') == destination_id:
            return dest
    
    # List available destinations
    available = [d.get('id') for d in config.get('destinations', []) if d.get('id')]
    raise ConfigError(
        f"Destination '{destination_id}' not found.\n"
        f"Available destinations: {', '.join(available) if available else 'none'}"
    )


def validate_destination_config(destination: Dict[str, Any], repo_root: Path) -> None:
    """
    Validate a destination configuration.
    
    Args:
        destination: Destination configuration dictionary
        repo_root: Repository root path for validating folder paths
        
    Raises:
        ConfigError: If configuration is invalid
    """
    # Required fields
    required_fields = ['id', 'name', 'confluence', 'source', 'credentials']
    for field in required_fields:
        if field not in destination:
            raise ConfigError(f"Missing required field: {field}")
    
    # Validate ID
    dest_id = destination['id']
    if not isinstance(dest_id, str) or not dest_id.strip():
        raise ConfigError("'id' must be a non-empty string")
    
    # Validate name
    if not isinstance(destination['name'], str) or not destination['name'].strip():
        raise ConfigError("'name' must be a non-empty string")
    
    # Validate confluence config
    confluence = destination['confluence']
    if not isinstance(confluence, dict):
        raise ConfigError("'confluence' must be a dictionary")
    
    required_confluence_fields = ['url', 'space_key', 'root_page_title']
    for field in required_confluence_fields:
        if field not in confluence:
            raise ConfigError(f"Missing required confluence field: {field}")
    
    if not isinstance(confluence['url'], str) or not confluence['url'].strip():
        raise ConfigError("'confluence.url' must be a non-empty string")
    
    if not isinstance(confluence['space_key'], str) or not confluence['space_key'].strip():
        raise ConfigError("'confluence.space_key' must be a non-empty string")
    
    if not isinstance(confluence['root_page_title'], str) or not confluence['root_page_title'].strip():
        raise ConfigError("'confluence.root_page_title' must be a non-empty string")
    
    # Validate source config
    source = destination['source']
    if not isinstance(source, dict):
        raise ConfigError("'source' must be a dictionary")
    
    if 'folders' not in source:
        raise ConfigError("'source.folders' is required")
    
    if not isinstance(source['folders'], list):
        raise ConfigError("'source.folders' must be a list")
    
    if len(source['folders']) == 0:
        raise ConfigError("At least one folder must be specified in 'source.folders'")
    
    # Validate each folder
    for idx, folder in enumerate(source['folders']):
        if not isinstance(folder, dict):
            raise ConfigError(f"'source.folders[{idx}]' must be a dictionary")
        
        if 'path' not in folder:
            raise ConfigError(f"'source.folders[{idx}].path' is required")
        
        folder_path = Path(folder['path'])
        if not folder_path.is_absolute():
            folder_path = repo_root / folder_path
        else:
            raise ConfigError(f"'source.folders[{idx}].path' must be a relative path")
        
        if not folder_path.exists():
            raise ConfigError(f"Folder not found: {folder['path']}")
        
        if not folder_path.is_dir():
            raise ConfigError(f"Not a directory: {folder['path']}")
        
        # Validate create_root_parent (optional, defaults to True)
        if 'create_root_parent' in folder:
            if not isinstance(folder['create_root_parent'], bool):
                raise ConfigError(f"'source.folders[{idx}].create_root_parent' must be a boolean")
        
        # Validate title (optional, custom title for folder page)
        if 'title' in folder:
            if not isinstance(folder['title'], str) or not folder['title'].strip():
                raise ConfigError(f"'source.folders[{idx}].title' must be a non-empty string")
    
    # Validate options
    options = destination.get('options', {})
    if not isinstance(options, dict):
        raise ConfigError("'options' must be a dictionary")
    
    # Validate force_sync_paths (optional)
        if 'force_sync_paths' in options:
            if not isinstance(options['force_sync_paths'], list):
                raise ConfigError("'options.force_sync_paths' must be a list")
            for idx, path in enumerate(options['force_sync_paths']):
                if not isinstance(path, str) or not path.strip():
                    raise ConfigError(f"'options.force_sync_paths[{idx}]' must be a non-empty string")
        
        if 'parallel_threads' in options:
            if not isinstance(options['parallel_threads'], int):
                raise ConfigError("'options.parallel_threads' must be an integer")
            if options['parallel_threads'] < 1 or options['parallel_threads'] > 50:
                raise ConfigError("'options.parallel_threads' must be between 1 and 50")
    
    # Validate credentials
    credentials = destination['credentials']
    if not isinstance(credentials, dict):
        raise ConfigError("'credentials' must be a dictionary")
    
    if 'username' not in credentials:
        raise ConfigError("'credentials.username' is required")
    
    if not isinstance(credentials['username'], str) or not credentials['username'].strip():
        raise ConfigError("'credentials.username' must be a non-empty string")
    
    if 'token_env_var' not in credentials:
        raise ConfigError("'credentials.token_env_var' is required")
    
    if not isinstance(credentials['token_env_var'], str) or not credentials['token_env_var'].strip():
        raise ConfigError("'credentials.token_env_var' must be a non-empty string")
    
    # Validate options (optional)
    if 'options' in destination:
        options = destination['options']
        if not isinstance(options, dict):
            raise ConfigError("'options' must be a dictionary")
        
        if 'add_git_metadata' in options:
            if not isinstance(options['add_git_metadata'], bool):
                raise ConfigError("'options.add_git_metadata' must be a boolean")
        
        if 'github_repo_override' in options:
            if options['github_repo_override'] is not None:
                if not isinstance(options['github_repo_override'], str):
                    raise ConfigError("'options.github_repo_override' must be a string or null")
        
        if 'dry_run' in options:
            if not isinstance(options['dry_run'], bool):
                raise ConfigError("'options.dry_run' must be a boolean")


def resolve_credentials(destination: Dict[str, Any]) -> Dict[str, str]:
    """
    Resolve credentials from environment variables.
    
    Args:
        destination: Destination configuration
        
    Returns:
        Dictionary with 'username' and 'token'
        
    Raises:
        ConfigError: If credentials cannot be resolved
    """
    credentials = destination['credentials']
    username = credentials['username']
    token_env_var = credentials['token_env_var']
    
    token = os.getenv(token_env_var)
    if not token:
        raise ConfigError(
            f"API token not found in environment variable '{token_env_var}'.\n"
            f"Set it with: export {token_env_var}=your-token"
        )
    
    return {
        'username': username,
        'token': token
    }


def get_repo_root() -> Path:
    """
    Get the repository root directory.
    
    Returns:
        Path to repository root
    """
    # scripts/ is in _confluence_sync/, which is in repo root
    script_dir = Path(__file__).parent
    return script_dir.parent.parent

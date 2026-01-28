#!/usr/bin/env python3
"""
Git utilities for extracting commit information and GitHub repository URLs.
"""

import subprocess
import re
from pathlib import Path
from typing import Optional, Tuple


def get_current_commit_hash(repo_root: Optional[Path] = None) -> Optional[str]:
    """
    Get the current Git commit hash.
    
    Args:
        repo_root: Repository root directory. If None, uses current directory.
        
    Returns:
        Commit hash (short format) or None if not a git repo or error
    """
    if repo_root is None:
        repo_root = Path.cwd()
    
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_full_commit_hash(repo_root: Optional[Path] = None) -> Optional[str]:
    """
    Get the full Git commit hash.
    
    Args:
        repo_root: Repository root directory. If None, uses current directory.
        
    Returns:
        Full commit hash or None if not a git repo or error
    """
    if repo_root is None:
        repo_root = Path.cwd()
    
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_github_repo_url(repo_root: Optional[Path] = None, override: Optional[str] = None) -> Optional[str]:
    """
    Get the GitHub repository URL for a file or directory.
    
    Args:
        repo_root: Repository root directory. If None, uses current directory.
        override: Override URL from config (takes precedence)
        
    Returns:
        GitHub repository URL (base URL) or None if not a GitHub repo or error
    """
    if override:
        return override.rstrip('/')
    
    if repo_root is None:
        repo_root = Path.cwd()
    
    try:
        # Get remote URL
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()
        
        # Convert to GitHub web URL
        # Handle both SSH and HTTPS formats
        # SSH: git@github.com:user/repo.git
        # HTTPS: https://github.com/user/repo.git
        # HTTPS with .git: https://github.com/user/repo.git
        
        # Remove .git suffix
        remote_url = remote_url.rstrip('.git')
        
        # Convert SSH to HTTPS
        if remote_url.startswith('git@github.com:'):
            remote_url = remote_url.replace('git@github.com:', 'https://github.com/')
        elif remote_url.startswith('git@'):
            # Handle other git hosts (gitlab, etc.) - convert to HTTPS
            remote_url = re.sub(r'git@([^:]+):', r'https://\1/', remote_url)
        
        # Ensure it's a GitHub URL
        if 'github.com' in remote_url:
            return remote_url
        
        return None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_file_github_url(
    file_path: Path,
    repo_root: Optional[Path] = None,
    github_repo_override: Optional[str] = None,
    commit_hash: Optional[str] = None
) -> Optional[str]:
    """
    Get the GitHub URL for a specific file at a specific commit.
    
    Args:
        file_path: Path to file (absolute or relative to repo_root)
        repo_root: Repository root directory
        github_repo_override: Override GitHub repo URL from config
        commit_hash: Commit hash (if None, uses current HEAD)
        
    Returns:
        Full GitHub URL to file at commit, or None if cannot determine
    """
    if repo_root is None:
        repo_root = Path.cwd()
    
    # Get GitHub repo URL
    repo_url = get_github_repo_url(repo_root, github_repo_override)
    if not repo_url:
        return None
    
    # Get commit hash if not provided
    if commit_hash is None:
        commit_hash = get_full_commit_hash(repo_root)
        if not commit_hash:
            return None
    
    # Get relative path from repo root
    try:
        if file_path.is_absolute():
            rel_path = file_path.relative_to(repo_root.resolve())
        else:
            rel_path = Path(file_path)
    except ValueError:
        # File is outside repo
        return None
    
    # Construct GitHub URL
    # Format: https://github.com/user/repo/blob/commit/path/to/file
    rel_path_str = str(rel_path).replace('\\', '/')
    return f"{repo_url}/blob/{commit_hash}/{rel_path_str}"


def get_file_commit_hash(file_path: Path, repo_root: Optional[Path] = None) -> Optional[str]:
    """
    Get the commit hash for the last commit that modified a specific file.
    
    Args:
        file_path: Path to the file (absolute or relative)
        repo_root: Repository root directory. If None, will be determined from file_path.
        
    Returns:
        Commit hash (short format) or None if not a git repo or error
    """
    if repo_root is None:
        repo_root = get_repo_root(file_path.parent if file_path.is_absolute() else None)
    
    if repo_root is None:
        return None
    
    try:
        # Get relative path from repo root
        if file_path.is_absolute():
            rel_path = file_path.relative_to(repo_root.resolve())
        else:
            rel_path = file_path
        
        # Get the commit hash for the last commit that modified this file
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%H', '--', str(rel_path)],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        commit_hash = result.stdout.strip()
        if commit_hash:
            # Return short format
            return commit_hash[:7]
        return None
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return None


def get_file_commit_date(file_path: Path, repo_root: Optional[Path] = None) -> Optional[str]:
    """
    Get the commit date for the last commit that modified a specific file.
    
    Args:
        file_path: Path to the file (absolute or relative)
        repo_root: Repository root directory. If None, will be determined from file_path.
        
    Returns:
        ISO format date string or None if not a git repo or error
    """
    if repo_root is None:
        repo_root = get_repo_root(file_path.parent if file_path.is_absolute() else None)
    
    if repo_root is None:
        return None
    
    try:
        # Get relative path from repo root
        if file_path.is_absolute():
            rel_path = file_path.relative_to(repo_root.resolve())
        else:
            rel_path = file_path
        
        # Get the commit date for the last commit that modified this file
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cI', '--', str(rel_path)],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        date_str = result.stdout.strip()
        return date_str if date_str else None
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return None


def get_repo_root(start_path: Optional[Path] = None) -> Optional[Path]:
    """
    Find the Git repository root directory.
    
    Args:
        start_path: Starting directory for search. If None, uses current directory.
        
    Returns:
        Path to repository root, or None if not in a git repo
    """
    if start_path is None:
        start_path = Path.cwd()
    else:
        start_path = Path(start_path).resolve()
    
    current = start_path
    
    while current != current.parent:
        git_dir = current / '.git'
        if git_dir.exists():
            return current
        current = current.parent
    
    return None

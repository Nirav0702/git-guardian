import sys
from pathlib import Path

# Use the standard library tomllib if available (Python 3.11+)
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

# Default configuration
DEFAULT_CONFIG = {
    "model": "codellama:latest",
    "block_on": ["security", "logic"],
    "warn_on": ["performance", "style"],
    "ignore_patterns": ["*.lock", "*.md"],
}

def load_config():
    """Loads configuration from .guardian.toml in the current git repo root."""
    config = DEFAULT_CONFIG.copy()
    
    # Find the root of the git repository
    git_root = Path.cwd()
    while not (git_root / ".git").exists() and git_root != git_root.parent:
        git_root = git_root.parent
    
    if not (git_root / ".git").exists():
        return config # Not in a git repo, return defaults

    config_path = git_root / ".guardian.toml"
    if config_path.exists():
        with open(config_path, "rb") as f:
            user_config = tomllib.load(f)
            config.update(user_config)
    return config
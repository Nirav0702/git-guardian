from pathlib import Path
import stat

HOOK_CONTENT = """
#!/bin/sh
# Git Guardian pre-commit hook

# Run the guardian analysis
guardian run
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "------------------------------------------------"
    echo "COMMIT REJECTED by Git Guardian."
    echo "Please fix the issues above before committing."
    echo "------------------------------------------------"
    exit 1
fi

exit 0
"""

def install_hook():
    """Installs the pre-commit hook script into the .git/hooks directory."""
    git_dir = Path.cwd() / ".git"
    if not git_dir.exists() or not git_dir.is_dir():
        print("❌ Error: Not a git repository. Please run `git init` first.")
        return

    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)
    
    pre_commit_hook_path = hooks_dir / "pre-commit"

    if pre_commit_hook_path.exists():
        print("⚠️ Warning: A pre-commit hook already exists. Overwriting.")

    with open(pre_commit_hook_path, "w") as f:
        f.write(HOOK_CONTENT)

    # Make the hook executable (chmod +x)
    pre_commit_hook_path.chmod(
        pre_commit_hook_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    )
    print("✅ Git Guardian hook installed successfully!")
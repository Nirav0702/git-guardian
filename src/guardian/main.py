import subprocess
import sys
import typer
from .config import load_config
from .analyzer import analyze_diff
from .installer import install_hook

app = typer.Typer()

@app.command()
def install():
    """Install the Git Guardian pre-commit hook."""
    install_hook()

@app.command(hidden=True)
def run():
    """The command executed by the git hook to analyze staged files."""
    config = load_config()
    
    try:
        diff = subprocess.check_output(['git', 'diff', '--cached']).decode('utf-8')
    except subprocess.CalledProcessError:
        print("❌ Error: Failed to get git diff. Are there any staged changes?")
        sys.exit(1)
        
    if not diff.strip():
        print("✅ No changes to analyze.")
        sys.exit(0)
    
    print("🤖 Git Guardian is analyzing your changes...")
    feedback = analyze_diff(diff, config["model"])

    if not feedback:
        # Analyzer already printed an error, exit with a generic code
        sys.exit(1)

    has_blocking_issue = False
    for issue_type, issues in feedback.items():
        if issues:
            is_blocking = issue_type in config["block_on"]
            is_warning = issue_type in config["warn_on"]
            
            if is_blocking:
                print(f"\n🚨 CRITICAL ({issue_type}):")
                has_blocking_issue = True
            elif is_warning:
                 print(f"\n⚠️ WARNING ({issue_type}):")
            else:
                continue # Ignore this issue type

            for issue in issues:
                print(f"   - {issue}")
    
    if has_blocking_issue:
        sys.exit(1) # Exit with non-zero to block commit

    print("\n✅ Git Guardian found no critical issues. Commit approved.")
    sys.exit(0)

if __name__ == "__main__":
    app()
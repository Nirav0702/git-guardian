# 🤖 Git Guardian AI

An intelligent Git pre-commit hook that uses a local Ollama LLM to automatically review your code changes before you commit them.

## Features

-   **Automated Code Review**: Catches potential bugs, security flaws, and performance issues.
-   **Local & Private**: Uses your own Ollama instance, so your code never leaves your machine.
-   **Configurable**: Easily configure the model, blocking rules, and ignored files.
-   **Easy Installation**: Get started in any Git repository with two commands.

## Installation

You need to have a running Ollama instance with a model pulled (e.g., `ollama pull codellama:latest`).

Install the package using pip:

```bash
pip install git-guardian-ai
````

## Usage
Navigate to your Git repository:

```bash
cd /path/to/your/project
````
**Run the install command**: This sets up the pre-commit hook in your repository's .git folder.

````bash
guardian install
````

**(Optional) Configure Guardian**: Create a .guardian.toml file in the root of your repository to customize the settings.

````bash
# .guardian.toml
model = "llama3:8b"
block_on = ["security", "logic"]
warn_on = ["performance", "style"]
````
Now, whenever you run git commit, the Guardian will automatically analyze your staged changes!

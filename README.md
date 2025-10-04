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

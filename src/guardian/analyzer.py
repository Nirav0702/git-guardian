import requests
import json

def analyze_diff(diff: str, model: str):
    """
    Analyzes a git diff using a local Ollama model.
    """
    # This is the most important part: The Prompt!
    # It instructs the model to act as a reviewer and return structured JSON.
    prompt = f"""
    You are an expert code reviewer acting as a Git pre-commit hook.
    Your task is to analyze the following code changes from a `git diff` and identify potential issues.
    Focus on:
    - Security vulnerabilities (e.g., hardcoded secrets, SQL injection).
    - Logic errors (e.g., off-by-one errors, null pointer issues).
    - Performance issues (e.g., N+1 queries, inefficient loops).
    - Code style or best practice violations.

    Analyze the diff provided below. Your response MUST be a single JSON object.
    The JSON object should have keys: "security", "logic", "performance", and "style".
    Each key should correspond to a list of strings, where each string is a concise description of an issue you found.
    If no issues are found for a category, provide an empty list.

    ```diff
    {diff}
    ```

    JSON Response:
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
            },
            timeout=60, # Add a timeout
        )
        response.raise_for_status()
        
        # The actual JSON string is in the 'response' key
        response_json_str = response.json().get('response', '{}')
        return json.loads(response_json_str)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Could not connect to Ollama. Is it running? Details: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Error: Failed to decode JSON response from the model. The model might be misconfigured.")
        return None
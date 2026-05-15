from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# API Key
api_key = os.getenv("GROQ_API_KEY")

print("Loaded Groq API Key:", api_key)

# Client
client = Groq(api_key=api_key)

def review_script(script):

    prompt = f"""
    You are a senior Zoho Deluge reviewer.

    Analyze this Deluge script for:
    1. Hardcoded IDs
    2. Null pointer risks
    3. Duplicate API calls
    4. Performance issues
    5. Security risks

    Provide:
    - Issue
    - Severity
    - Suggestion

    Script:
    {script}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
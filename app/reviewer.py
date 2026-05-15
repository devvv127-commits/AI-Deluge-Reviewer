from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
from monitoring import tracer
import os
import time


# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# API Key
api_key = os.getenv("GROQ_API_KEY")

# Validate API Key
if not api_key:
    raise ValueError(
        "❌ GROQ_API_KEY not found in .env file.\n"
        "Please create a .env file in the project root.\n"
        "See .env.example for the required format."
    )

print("✓ Groq API Key loaded successfully")

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

def review_script(script):

    with tracer.start_as_current_span("ai-deluge-review"):

        start = time.time()

        # AI logic here

        duration = time.time() - start

        print(f"Review completed in {duration} seconds")

    return response.choices[0].message.content
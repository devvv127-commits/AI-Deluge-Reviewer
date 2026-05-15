# AI Deluge Reviewer

An AI-powered code review tool for the Deluge project using Groq's language model.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Then edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from: https://console.groq.com

### 3. Run the Reviewer
```bash
python app/main.py
```

This will:
- Read `sample_scripts/bad_script.dg`
- Analyze it with AI for code issues
- Generate `reports/report.html`

## Features

The AI reviews Deluge scripts for:
- Hardcoded IDs
- Null pointer risks
- Duplicate API calls
- Performance issues
- Security risks

## Security

- **Never commit `.env` files** - they contain API keys
- `.env` is in `.gitignore` by default
- Use `.env.example` as a template for new developers

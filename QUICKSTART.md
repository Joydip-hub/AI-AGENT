# AI-AGENT Quick Start Guide

## Installation (5 minutes)

### Step 1: Setup Environment
```bash
cd AI-AGENT
python setup.py
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Chatbot
```bash
# Simple version (no extra dependencies)
python chat.py

# Full version (with colors and features)
python main.py
```

## Quick Test

Try these multilingual greetings:
- English: "Hello!"
- Spanish: "¡Hola!"
- Hindi: "नमस्ते!"
- French: "Bonjour!"
- Tamil: "வணக்கம்!"

## Commands
- `quit` - Exit
- `help` - Show commands
- `stats` - View statistics
- `clear` - Clear history

## Next Steps
1. Add API keys to `.env` for production AI models
2. Customize `config/config.yaml` for your needs
3. Run examples: `python examples/example_usage.py`
4. Run tests: `pytest tests/`

## File Structure
```
AI-AGENT/
├── src/               # Core modules
├── config/            # Configuration files
├── examples/          # Usage examples
├── tests/             # Unit tests
├── main.py            # Full CLI app
└── chat.py            # Simple CLI app
```

Enjoy your multilingual AI chatbot!

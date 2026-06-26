# AI-AGENT Installation Guide

## Super Simple Installation (Recommended)

Install AI-AGENT directly from GitHub and use it anywhere in your terminal!

### One-Line Installation

```bash
pip install git+https://github.com/Joydip-hub/AI-AGENT.git
```

That's it! Now you can use AI-AGENT from anywhere.

---

## Usage

### Method 1: Terminal Command (Anywhere)

After installation, simply type:

```bash
ai-agent
```

That's it! The chatbot starts immediately in any terminal, from any directory.

### Method 2: Simple Mode

For a basic interface:

```bash
ai-agent-simple
```

---

## Quick Start

1. **Install**
   ```bash
   pip install git+https://github.com/Joydip-hub/AI-AGENT.git
   ```

2. **Run**
   ```bash
   ai-agent
   ```

3. **Chat**
   ```
   You: Hello!
   Agent: Hello! I'm your AI assistant...
   ```

4. **Try Different Languages**
   ```
   You: नमस्ते!
   Agent: नमस्ते! मैं आपका AI सहायक हूं...
   ```

---

## Available Commands

Once the chatbot is running:

| Command | Description |
|---------|-------------|
| `help` | Show available commands |
| `stats` | View conversation statistics |
| `clear` | Clear conversation history |
| `export` | Save conversation to file |
| `lang` | Show detected language |
| `quit` | Exit the chatbot |

---

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for installation only)

---

## Platform-Specific Instructions

### Windows

1. Open Command Prompt or PowerShell
2. Run:
   ```bash
   pip install git+https://github.com/Joydip-hub/AI-AGENT.git
   ```
3. Start:
   ```bash
   ai-agent
   ```

### macOS / Linux

1. Open Terminal
2. Run:
   ```bash
   pip3 install git+https://github.com/Joydip-hub/AI-AGENT.git
   ```
3. Start:
   ```bash
   ai-agent
   ```

---

## Alternative Installation Methods

### Method 1: Clone and Install

```bash
# Clone repository
git clone https://github.com/Joydip-hub/AI-AGENT.git
cd AI-AGENT

# Install in development mode
pip install -e .

# Run from anywhere
ai-agent
```

### Method 2: Download and Install

1. Download ZIP from GitHub
2. Extract to a folder
3. Open terminal in that folder
4. Run:
   ```bash
   pip install .
   ```
5. Use `ai-agent` command anywhere

---

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade git+https://github.com/Joydip-hub/AI-AGENT.git
```

---

## Uninstallation

To remove AI-AGENT:

```bash
pip uninstall ai-agent
```

---

## Troubleshooting

### Issue: "pip not found"
**Solution:**
```bash
# Windows
python -m pip install git+https://github.com/Joydip-hub/AI-AGENT.git

# macOS/Linux
python3 -m pip install git+https://github.com/Joydip-hub/AI-AGENT.git
```

### Issue: "ai-agent command not found"
**Solution:**
```bash
# Add Python scripts to PATH, or use:
python -m src.cli
```

### Issue: Permission denied
**Solution (macOS/Linux):**
```bash
sudo pip3 install git+https://github.com/Joydip-hub/AI-AGENT.git
```

### Issue: Dependencies fail to install
**Solution:**
```bash
# Upgrade pip first
pip install --upgrade pip setuptools wheel

# Then install AI-AGENT
pip install git+https://github.com/Joydip-hub/AI-AGENT.git
```

---

## Verification

To verify installation:

```bash
# Check if installed
pip show ai-agent

# Try running
ai-agent
```

You should see the AI-AGENT welcome screen.

---

## 40+ Languages Supported

Try chatting in any of these languages:

**European:** English, Spanish, French, German, Italian, Portuguese, Russian, Polish, Dutch, Swedish

**Indian:** Hindi (हिंदी), Tamil (தமிழ்), Telugu (తెలుగు), Bengali (বাংলা), Marathi (मराठी), Gujarati (ગુજરાતી)

**East Asian:** Chinese (中文), Japanese (日本語), Korean (한국어)

**Middle Eastern:** Arabic (العربية), Persian (فارسی), Hebrew (עברית)

**And many more!**

---

## Examples

### English
```
You: What is artificial intelligence?
Agent: Artificial Intelligence (AI) is...
```

### Hindi
```
You: कृत्रिम बुद्धिमत्ता क्या है?
Agent: कृत्रिम बुद्धिमत्ता (AI) एक...
```

### Spanish
```
You: ¿Qué es la inteligencia artificial?
Agent: La Inteligencia Artificial (IA) es...
```

---

## Getting Help

- 📖 Documentation: [README.md](README.md)
- 🐛 Report Issues: [GitHub Issues](https://github.com/Joydip-hub/AI-AGENT/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/Joydip-hub/AI-AGENT/discussions)

---

## Summary

**Installation:**
```bash
pip install git+https://github.com/Joydip-hub/AI-AGENT.git
```

**Usage:**
```bash
ai-agent
```

**That's it!** Enjoy your multilingual AI chatbot! 🤖🌍

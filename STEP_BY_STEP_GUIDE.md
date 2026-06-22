# Complete Step-by-Step Guide to Access AI-AGENT Chatbot

## Prerequisites Check

Before starting, ensure you have:
- Windows, macOS, or Linux operating system
- Internet connection (for downloading dependencies)
- Text editor (Notepad++, VS Code, or any text editor)

---

## STEP 1: Install Python

### Option A: Windows
1. Open your web browser
2. Go to: https://www.python.org/downloads/
3. Click the yellow "Download Python 3.x.x" button
4. Run the downloaded installer (.exe file)
5. **IMPORTANT**: Check "Add Python to PATH" checkbox
6. Click "Install Now"
7. Wait for installation to complete
8. Click "Close"

### Option B: macOS
1. Open Terminal (Applications > Utilities > Terminal)
2. Install Homebrew if not installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python:
   ```bash
   brew install python
   ```

### Option C: Linux (Ubuntu/Debian)
1. Open Terminal
2. Run these commands:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

### Verify Python Installation
1. Open Command Prompt (Windows) or Terminal (Mac/Linux)
2. Type: `python --version` or `python3 --version`
3. You should see: `Python 3.x.x`
4. Type: `pip --version` or `pip3 --version`
5. You should see pip version information

---

## STEP 2: Navigate to AI-AGENT Directory

### Windows:
1. Open Command Prompt:
   - Press `Windows Key + R`
   - Type `cmd`
   - Press Enter
2. Navigate to AI-AGENT folder:
   ```cmd
   cd C:\Users\JOYG\AI-AGENT
   ```

### Mac/Linux:
1. Open Terminal
2. Navigate to AI-AGENT folder:
   ```bash
   cd ~/AI-AGENT
   ```
   Or if in different location:
   ```bash
   cd /path/to/AI-AGENT
   ```

### Verify You're in the Right Place
Type this command:
```bash
dir         # Windows
ls          # Mac/Linux
```

You should see these files:
- main.py
- chat.py
- setup.py
- requirements.txt
- README.md

---

## STEP 3: Set Up the Environment

### Run the Setup Script
Type and press Enter:
```bash
python setup.py
```

You should see output like:
```
============================================================
   AI-AGENT Setup
============================================================

Python version: 3.x.x
Created directory: data/conversations
Created directory: logs
Created directory: models
Created directory: cache

Setup complete!
```

---

## STEP 4: Install Required Libraries

### Install All Dependencies
Type this command and press Enter:
```bash
pip install -r requirements.txt
```

**This will take 2-5 minutes.** You'll see many packages being downloaded and installed:
- openai
- langdetect
- flask
- colorama
- And many more...

Wait until you see:
```
Successfully installed [list of packages]
```

### If You Get Errors:
Try using `pip3` instead:
```bash
pip3 install -r requirements.txt
```

Or use Python module installation:
```bash
python -m pip install -r requirements.txt
```

---

## STEP 5: Choose Your Chatbot Interface

You have TWO options:

### Option A: Simple Chatbot (Recommended for Beginners)
- Basic text interface
- No extra dependencies needed
- Works on any system

### Option B: Advanced Chatbot (Recommended for Better Experience)
- Colored text interface
- More features and commands
- Better user experience

---

## STEP 6: Start the Chatbot

### Option A: Simple Chatbot

1. Type this command:
   ```bash
   python chat.py
   ```

2. You should see:
   ```
   ============================================================
      AI-AGENT: Multilingual AI Chatbot
      Type 'quit' to exit, 'help' for commands
   ============================================================

   Chatbot ready! Start typing in any language...

   You: 
   ```

3. Start chatting! Type any message and press Enter.

### Option B: Advanced Chatbot

1. Type this command:
   ```bash
   python main.py
   ```

2. You should see a colorful interface:
   ```
   ============================================================
      AI-AGENT: Multilingual AI Chatbot
      Supports 40+ languages including regional variants
   ============================================================

   Chatbot initialized! Type '/help' for commands or start chatting.
   You can type in any language, and I'll respond accordingly!

   You: 
   ```

3. Start chatting! Type any message and press Enter.

---

## STEP 7: Test the Chatbot

### Test 1: English Greeting
Type:
```
Hello! How are you?
```
Press Enter.

You should get a response like:
```
Agent: Hello! I'm your AI assistant. I can help you with any topic...
```

### Test 2: Hindi Greeting
Type:
```
नमस्ते! आप कैसे हैं?
```
Press Enter.

The bot will detect Hindi and respond in Hindi!

### Test 3: Spanish Greeting
Type:
```
¡Hola! ¿Cómo estás?
```
Press Enter.

The bot will detect Spanish and respond in Spanish!

### Test 4: Ask a Question
Type:
```
What is artificial intelligence?
```
Press Enter.

The bot will provide information about AI.

---

## STEP 8: Use Chatbot Commands

### Available Commands (Simple Version - chat.py):
- `help` - Show available commands
- `stats` - Show conversation statistics
- `clear` - Clear conversation history
- `quit` or `exit` - Exit the chatbot

### Available Commands (Advanced Version - main.py):
- `/help` - Show available commands
- `/stats` - Show conversation statistics
- `/clear` - Clear conversation history
- `/export` - Export conversation to file
- `/lang` - Show detected language
- `/quit` - Exit the chatbot

### Try These Commands:

1. View statistics:
   ```
   stats        # For simple version
   /stats       # For advanced version
   ```

2. Clear history:
   ```
   clear        # For simple version
   /clear       # For advanced version
   ```

3. Get help:
   ```
   help         # For simple version
   /help        # For advanced version
   ```

---

## STEP 9: Test Multiple Languages

Try these greetings in different languages:

### Indian Languages:
```
नमस्ते!                    (Hindi)
வணக்கம்!                   (Tamil)
నమస్కారం!                  (Telugu)
നമസ്കാരം!                 (Malayalam)
ನಮಸ್ಕಾರ!                   (Kannada)
નમસ્તે!                    (Gujarati)
নমস্কার!                   (Bengali)
```

### European Languages:
```
Bonjour!                   (French)
¡Hola!                     (Spanish)
Hallo!                     (German)
Ciao!                      (Italian)
Olá!                       (Portuguese)
```

### Asian Languages:
```
你好!                       (Chinese)
こんにちは!                 (Japanese)
안녕하세요!                 (Korean)
สวัสดี!                     (Thai)
```

### Middle Eastern Languages:
```
مرحبا!                     (Arabic)
سلام!                      (Persian)
שלום!                      (Hebrew)
```

---

## STEP 10: Exit the Chatbot

When you're done:

### Simple Version (chat.py):
Type:
```
quit
```
or
```
exit
```

### Advanced Version (main.py):
Type:
```
/quit
```
or press `Ctrl + C`

---

## Troubleshooting Common Issues

### Issue 1: "Python is not recognized"
**Solution:**
1. Reinstall Python
2. Make sure to check "Add Python to PATH" during installation
3. Restart your Command Prompt/Terminal

### Issue 2: "No module named 'langdetect'"
**Solution:**
```bash
pip install langdetect
```

### Issue 3: "Permission denied" error
**Solution (Windows):**
Run Command Prompt as Administrator

**Solution (Mac/Linux):**
```bash
sudo python chat.py
```

### Issue 4: Chatbot responds in wrong language
**Solution:**
Type `/clear` to clear history, then try again with a longer sentence in your desired language.

### Issue 5: "ModuleNotFoundError"
**Solution:**
Reinstall all dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

---

## Advanced Usage

### Export Your Conversation (Advanced Version Only)
1. Chat with the bot
2. Type: `/export`
3. Your conversation is saved to: `data/conversation_[session_id].json`

### View Conversation Statistics
1. Chat for a while
2. Type: /stats (or stats in simple version)
3. See:
   - Total messages
   - Languages used
   - Session duration

### Save Your Session
Your session is automatically saved when you:
- Type /quit
- Press Ctrl + C

---

## Pro Tips

### Tip 1: Better Language Detection
Use complete sentences instead of single words for better language detection.

**Good:**
```
How are you doing today?
```

**Not as good:**
```
Hi
```

### Tip 2: Switching Languages
You can switch languages mid-conversation! Just start typing in a different language.

### Tip 3: Ask Anything
The chatbot has knowledge about:
- Science (physics, chemistry, biology)
- Technology (AI, programming, web development)
- Mathematics (algebra, calculus, geometry)
- History (ancient, modern, world wars)
- Arts (music, painting, literature)
- And many more topics!

### Tip 4: Context Awareness
The chatbot remembers your previous messages in the conversation, so you can ask follow-up questions.

---

## Running Examples and Tests

### Run Example Demonstrations
```bash
python examples/example_usage.py
```

This will show you:
- Basic conversation examples
- Multilingual conversation demos
- Conversation management examples
- Language detection examples
- Knowledge base usage
- Statistics examples

### Run Unit Tests
```bash
pytest tests/
```

Or with detailed output:
```bash
pytest tests/ -v
```

---

## Video Tutorial Format (Step Summary)

If you prefer video-style instructions, follow these numbered steps:

**Part 1: Installation (5 minutes)**
1. [00:00-01:00] Install Python from python.org
2. [01:00-02:00] Open Command Prompt/Terminal
3. [02:00-03:00] Navigate to AI-AGENT folder
4. [03:00-04:00] Run setup.py
5. [04:00-05:00] Install requirements.txt

**Part 2: First Run (2 minutes)**
6. [00:00-00:30] Run python chat.py
7. [00:30-01:00] Type "Hello!"
8. [01:00-01:30] Try different languages
9. [01:30-02:00] Type "quit" to exit

**Part 3: Advanced Features (3 minutes)**
10. [00:00-01:00] Run python main.py
11. [01:00-02:00] Try /help, /stats commands
12. [02:00-03:00] Export conversation with /export

---

## Complete Command Reference

### Simple Version (chat.py) Commands:
| Command | Description |
|---------|-------------|
| help | Show available commands |
| stats | Display conversation statistics |
| clear | Clear conversation history |
| quit | Exit the chatbot |
| exit | Exit the chatbot |
| bye | Exit the chatbot |

### Advanced Version (main.py) Commands:
| Command | Description |
|---------|-------------|
| /help | Show available commands |
| /stats | Display detailed statistics |
| /clear | Clear conversation history |
| /export | Export conversation to JSON file |
| /lang | Show currently detected language |
| /quit | Exit the chatbot |
| /exit | Exit the chatbot |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Send message |
| Ctrl + C | Emergency exit (saves session) |
| Up Arrow | Recall last command (terminal feature) |
| Ctrl + L | Clear terminal screen (terminal feature) |

---

## Frequently Asked Questions (FAQ)

### Q1: Do I need an internet connection?
**A:** The basic chatbot works offline with template responses. For full AI capabilities, you need to add API keys and have internet connection.

### Q2: How do I add API keys for real AI responses?
**A:** 
1. Copy .env.example to .env
2. Edit .env file
3. Add your OpenAI, Anthropic, or Google AI API key
4. Restart the chatbot

### Q3: Which languages are supported?
**A:** 40+ languages including:
- All major European languages
- All Indian regional languages (Hindi, Tamil, Telugu, etc.)
- East Asian languages (Chinese, Japanese, Korean)
- Middle Eastern languages (Arabic, Persian, Hebrew)
- Southeast Asian languages (Thai, Vietnamese, Indonesian)

### Q4: Can I use this for my own project?
**A:** Yes! This project is MIT licensed. You can use, modify, and distribute it freely.

### Q5: How do I stop the chatbot?
**A:** Type quit or /quit depending on which version you're using.

### Q6: Where are conversations saved?
**A:** Conversations are saved in data/conversations/ folder as JSON files.

### Q7: Can I customize the chatbot?
**A:** Yes! Edit the files in src/ folder to customize behavior, add features, or modify responses.

### Q8: How do I update the knowledge base?
**A:** Edit src/knowledge_base.py and add your own topics and information.

### Q9: Can multiple people use it at the same time?
**A:** The current version is single-user. For multi-user support, you'd need to implement a web interface.

### Q10: What if I get errors?
**A:** Check the Troubleshooting section above, or check the logs in logs/ folder.

---

## Next Steps After Setup

### Beginner Path:
1. ? Complete this guide
2. ? Test basic chatting
3. ? Try different languages
4. ?? Read README.md for features
5. ?? Run example_usage.py

### Intermediate Path:
1. ? Complete beginner path
2. ?? Add API keys for real AI
3. ?? Customize knowledge base
4. ?? Modify conversation settings
5. ?? Run and understand tests

### Advanced Path:
1. ? Complete intermediate path
2. ?? Study the source code in src/
3. ?? Add new features
4. ?? Integrate with web framework
5. ?? Deploy as web service

---

## Getting Help

If you need help:
1. Check this guide again
2. Read README.md
3. Check example_usage.py
4. Review source code comments
5. Create an issue on GitHub

---

## Conclusion

**Congratulations!** You now know how to:
- ? Install Python and dependencies
- ? Set up AI-AGENT
- ? Start the chatbot
- ? Chat in multiple languages
- ? Use commands and features
- ? Troubleshoot common issues

**Start chatting now:**
```bash
cd AI-AGENT
python chat.py
```

Enjoy your multilingual AI chatbot! ????

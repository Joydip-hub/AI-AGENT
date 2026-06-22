# AI-AGENT: Multilingual AI Chatbot

A powerful AI chatbot agent that can converse in multiple languages including regional variants and answer questions on any topic.

## Features

- **Multilingual Support**: Communicate in 40+ languages including regional languages (Hindi, Tamil, Telugu, Bengali, Gujarati, Kannada, Malayalam, Marathi, Punjabi, Urdu, and more)
- **Universal Knowledge**: Answer questions on any topic including science, technology, history, mathematics, arts, and more
- **Conversation Management**: Maintains context across conversations with session management
- **Language Detection**: Automatically detects and responds in the user's language
- **Extensible Architecture**: Modular design for easy customization and extension

## Supported Languages

### Major World Languages
- English, Spanish, French, German, Italian, Portuguese, Russian
- Chinese (Simplified & Traditional), Japanese, Korean
- Arabic, Turkish, Persian, Hebrew

### Regional Indian Languages
- Hindi (हिंदी)
- Bengali (বাংলা)
- Telugu (తెలుగు)
- Tamil (தமிழ்)
- Marathi (मराठी)
- Gujarati (ગુજરાતી)
- Kannada (ಕನ್ನಡ)
- Malayalam (മലയാളം)
- Punjabi (ਪੰਜਾਬੀ)
- Urdu (اردو)
- Odia (ଓଡ଼ିଆ)

### Southeast Asian Languages
- Thai, Vietnamese, Indonesian, Malay, Filipino, Burmese, Khmer, Lao

### Other Languages
- Polish, Ukrainian, Romanian, Dutch, Swedish, Danish, Norwegian, Finnish
- Czech, Greek, Swahili, Amharic, Nepali, Sinhala

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AI-AGENT.git
cd AI-AGENT
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys (optional):
```bash
# Copy the example config
cp config/config.example.yaml config/config.yaml

# Edit config.yaml with your API keys
# For production use, integrate with OpenAI, Anthropic, or Google AI
```

## Quick Start

### Basic Usage

```python
from src.ai_agent import AIAgent

# Initialize the AI agent
agent = AIAgent()

# Process a message
response = agent.process_input("Hello! How are you?")
print(response['content'])

# Multilingual example - Hindi
response = agent.process_input("नमस्ते! आप कैसे हैं?")
print(response['content'])

# Ask about any topic
response = agent.process_input("What is quantum physics?")
print(response['content'])
```

### Using Conversation Manager

```python
from src.conversation_manager import ConversationManager
from src.ai_agent import AIAgent

# Initialize components
conv_manager = ConversationManager()
agent = AIAgent()

# Create a session
session_id = "user_123_session_1"
conv_manager.create_session(session_id, user_info={'name': 'John'})

# Process messages
user_input = "Tell me about artificial intelligence"
response = agent.process_input(user_input)

# Add to conversation history
conv_manager.add_message(session_id, 'user', user_input)
conv_manager.add_message(session_id, 'assistant', response['content'])

# Get conversation context
context = conv_manager.get_context(session_id, limit=5)
print(context)

# Save session
conv_manager.save_session(session_id)
```

### Using Knowledge Base

```python
from src.knowledge_base import KnowledgeBase

# Initialize knowledge base
kb = KnowledgeBase()

# Search for information
results = kb.search_knowledge("artificial intelligence")
print(results)

# Get specific category
science = kb.get_category("science")
print(science)

# Get all categories
categories = kb.get_all_categories()
print(categories)
```

## Project Structure

```
AI-AGENT/
├── src/
│   ├── ai_agent.py              # Main AI agent implementation
│   ├── language_detector.py     # Language detection module
│   ├── conversation_manager.py  # Conversation management
│   └── knowledge_base.py        # Knowledge base integration
├── config/
│   └── config.example.yaml      # Example configuration
├── data/
│   └── conversations/           # Stored conversations
├── tests/
│   └── test_ai_agent.py        # Unit tests
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## Configuration

Create a `config/config.yaml` file:

```yaml
agent:
  default_language: en
  auto_detect_language: true
  max_history: 50
  
model:
  name: gpt-3.5-turbo
  temperature: 0.7
  max_tokens: 2000

api_keys:
  openai: YOUR_OPENAI_KEY
  anthropic: YOUR_ANTHROPIC_KEY
  google: YOUR_GOOGLE_AI_KEY
```

## Advanced Usage

### Custom Configuration

```python
config = {
    'max_history': 100,
    'default_language': 'hi',  # Hindi
    'auto_detect_language': True,
    'temperature': 0.8
}

agent = AIAgent(config=config)
```

### Export Conversations

```python
# Export conversation history
agent.export_conversation('conversation_export.json')
```

### Get Statistics

```python
# Get conversation statistics
stats = agent.get_statistics()
print(f"Total messages: {stats['total_messages']}")
print(f"Languages used: {stats['languages_used']}")
```

## Integration with AI Models

To integrate with production AI models, modify the `_generate_intelligent_response` method in `ai_agent.py`:

### OpenAI Integration

```python
import openai

def _generate_intelligent_response(self, user_input, language, context):
    openai.api_key = self.config.get('openai_api_key')
    
    messages = [
        {"role": "system", "content": self._build_system_prompt(language)},
        *[{"role": m['role'], "content": m['content']} for m in context],
        {"role": "user", "content": user_input}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return response.choices[0].message.content
```

## Testing

Run the test suite:

```bash
pytest tests/
```

Run with coverage:

```bash
pytest --cov=src tests/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Acknowledgments

- Language detection powered by langdetect
- Supports integration with OpenAI, Anthropic, and Google AI APIs
- Built with Python and modern NLP libraries

## Roadmap

- [ ] Add voice input/output support
- [ ] Implement real-time translation
- [ ] Add sentiment analysis
- [ ] Create web interface
- [ ] Mobile app integration
- [ ] Add more knowledge domains
- [ ] Implement RAG (Retrieval Augmented Generation)
- [ ] Add image understanding capabilities

"""
Configuration Settings for AI-AGENT
"""

# Agent Configuration
AGENT_CONFIG = {
    'max_history': 50,
    'default_language': 'en',
    'auto_detect_language': True,
    'temperature': 0.7,
    'max_tokens': 2000
}

# Model Configuration
MODEL_CONFIG = {
    'model_name': 'gpt-3.5-turbo',
    'provider': 'openai',  # openai, anthropic, google
    'fallback_model': 'gpt-3.5-turbo'
}

# Language Settings
LANGUAGE_CONFIG = {
    'supported_languages': [
        'en', 'es', 'fr', 'de', 'it', 'pt', 'ru',
        'zh-cn', 'zh-tw', 'ja', 'ko', 'ar',
        'hi', 'bn', 'te', 'ta', 'mr', 'gu', 'kn', 'ml', 'pa', 'ur', 'or',
        'th', 'vi', 'id', 'ms', 'fil', 'tr', 'pl', 'uk', 'ro', 'nl',
        'sv', 'da', 'no', 'fi', 'cs', 'el', 'he', 'fa', 'sw', 'am', 'ne', 'si', 'my', 'km', 'lo'
    ],
    'default_fallback': 'en'
}

# Conversation Settings
CONVERSATION_CONFIG = {
    'storage_path': './data/conversations',
    'auto_save': True,
    'context_window': 10,
    'session_timeout_minutes': 30
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': './logs/ai_agent.log',
    'max_bytes': 10485760,  # 10MB
    'backup_count': 5
}

# API Keys (Set via environment variables)
API_KEYS = {
    'openai': None,  # Set OPENAI_API_KEY env variable
    'anthropic': None,  # Set ANTHROPIC_API_KEY env variable
    'google': None  # Set GOOGLE_API_KEY env variable
}

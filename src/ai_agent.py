"""
AI Chatbot Agent - Main Application
Multilingual conversational AI with support for multiple topics and languages
"""

import os
import sys
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class AIAgent:
    """
    Main AI Agent class for multilingual chatbot
    Handles conversations across multiple languages and topics
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the AI Agent
        
        Args:
            config: Configuration dictionary
        """
        self.logger = logging.getLogger(__name__)
        self.config = config or self._load_default_config()
        self.conversation_history = []
        self.current_language = 'en'
        self.user_preferences = {}
        
        # Import language detector
        try:
            from language_detector import LanguageDetector
            self.language_detector = LanguageDetector()
        except ImportError:
            self.logger.warning("Language detector not available")
            self.language_detector = None
        
        self.logger.info("AI Agent initialized successfully")
    
    def _load_default_config(self) -> Dict:
        """Load default configuration"""
        return {
            'max_history': 50,
            'default_language': 'en',
            'auto_detect_language': True,
            'model_name': 'gpt-3.5-turbo',
            'temperature': 0.7,
            'max_tokens': 2000
        }
    
    def detect_and_set_language(self, text: str) -> str:
        """
        Detect language from user input and set as current
        
        Args:
            text: User input text
            
        Returns:
            Detected language code
        """
        if not self.language_detector or not self.config.get('auto_detect_language'):
            return self.current_language
        
        try:
            detected_lang = self.language_detector.detect_language(text)
            if detected_lang and self.language_detector.is_supported(detected_lang):
                self.current_language = detected_lang
                self.logger.info(f"Language detected: {detected_lang}")
            return detected_lang
        except Exception as e:
            self.logger.error(f"Language detection error: {e}")
            return self.current_language
    
    def add_to_history(self, role: str, content: str, language: Optional[str] = None):
        """
        Add message to conversation history
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
            language: Language code
        """
        message = {
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'language': language or self.current_language
        }
        
        self.conversation_history.append(message)
        
        # Limit history size
        max_history = self.config.get('max_history', 50)
        if len(self.conversation_history) > max_history:
            self.conversation_history = self.conversation_history[-max_history:]
    
    def get_conversation_context(self, limit: int = 10) -> List[Dict]:
        """
        Get recent conversation context
        
        Args:
            limit: Number of recent messages to retrieve
            
        Returns:
            List of recent messages
        """
        return self.conversation_history[-limit:]
    
    def process_input(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input and generate response
        
        Args:
            user_input: User's message
            
        Returns:
            Response dictionary with message and metadata
        """
        # Detect language
        detected_lang = self.detect_and_set_language(user_input)
        
        # Add to history
        self.add_to_history('user', user_input, detected_lang)
        
        # Generate response
        response = self._generate_response(user_input, detected_lang)
        
        # Add response to history
        self.add_to_history('assistant', response['content'], detected_lang)
        
        return response
    
    def _generate_response(self, user_input: str, language: str) -> Dict[str, Any]:
        """
        Generate AI response based on user input
        
        Args:
            user_input: User's message
            language: Detected language
            
        Returns:
            Response dictionary
        """
        # Get conversation context
        context = self.get_conversation_context()
        
        # Build system prompt with multilingual capability
        system_prompt = self._build_system_prompt(language)
        
        # For now, return a template response
        # In production, this would call actual AI models (OpenAI, Anthropic, etc.)
        response_content = self._generate_intelligent_response(user_input, language, context)
        
        return {
            'content': response_content,
            'language': language,
            'timestamp': datetime.now().isoformat(),
            'metadata': {
                'model': self.config.get('model_name'),
                'context_length': len(context)
            }
        }
    
    def _build_system_prompt(self, language: str) -> str:
        """
        Build system prompt for AI model
        
        Args:
            language: Target language
            
        Returns:
            System prompt string
        """
        language_name = self.language_detector.get_language_name(language) if self.language_detector else language
        
        return f"""You are an advanced multilingual AI assistant capable of conversing in any language.
Current conversation language: {language_name} ({language})

Your capabilities:
- Answer questions on any topic with accurate, comprehensive information
- Understand and respond in multiple languages including regional variants
- Maintain context across conversation history
- Provide helpful, informative, and engaging responses
- Adapt your communication style to the user's language and culture

Always respond in the same language as the user's input unless explicitly asked to translate."""
    
    def _generate_intelligent_response(self, user_input: str, language: str, context: List[Dict]) -> str:
        """"""
        Generate intelligent response using AI models
        
        Args:
            user_input: User's input
            language: Language code
            context: Conversation context
            
        Returns:
            Generated response
        """"""
        # This is a placeholder for actual AI model integration
        # In production, integrate with OpenAI, Anthropic, Google AI, etc.
        
        user_input_lower = user_input.lower()
        
        # Basic response templates for different languages
        responses = {
            'greeting': {
                'en': "Hello! I'm your AI assistant. I can help you with any topic and communicate in multiple languages. What would you like to know?",
                'hi': "??????! ??? ???? AI ????? ???? ??? ???? ?? ???? ??? ???? ??? ?? ???? ??? ?? ?? ?????? ??? ??? ?? ???? ???? ?? ???? ????? ????????",
                'es': "¡Hola! Soy tu asistente de IA. Puedo ayudarte con cualquier tema y comunicarme en varios idiomas. ¿Qué te gustaría saber?",
                'fr': "Bonjour! Je suis votre assistant IA. Je peux vous aider sur n'importe quel sujet et communiquer dans plusieurs langues. Que souhaitez-vous savoir?",
                'de': "Hallo! Ich bin dein KI-Assistent. Ich kann dir bei jedem Thema helfen und in mehreren Sprachen kommunizieren. Was möchtest du wissen?",
                'zh-cn': "??!????AI???????????????,??????????????????",
                'ja': "?????!??????AI???????????????????????????????????????????????????????",
                'ar': "?????! ??? ?????? ?????. ?????? ??????? ?? ?? ????? ???????? ????? ??????. ???? ???? ?? ?????",
                'ta': "???????! ???? ?????? AI ?????????. ???? ???? ??????????? ?????????? ??? ???????? ??????? ?? ????????? ??????? ????? ????????. ??????? ???? ???????? ????? ??????????????????",
                'te': "????????! ???? ?? AI ??????????. ???? ? ?????????? ???? ????? ??????? ????? ???? ?????? ??????????? ???????. ???? ??? ?????????????????????????",
                'pt': "Olá! Sou seu assistente de IA. Posso ajudá-lo com qualquer tópico e me comunicar em vários idiomas. O que você gostaria de saber?",
                'ru': "????????????! ? ??? AI-?????????. ???? ?????? ? ????? ????? ? ???????? ?? ?????????? ??????. ??? ?? ?? ?????? ???????"
            }
        }
        
        # Simple greeting detection
        greetings = ['hello', 'hi', 'hey', 'namaste', '??????', 'hola', 'bonjour', 'hallo', '??', '?????', '?????', '???????', '????????']
        if any(greeting in user_input_lower for greeting in greetings):
            return responses['greeting'].get(language, responses['greeting']['en'])
        
        # Default response
        return f"I understand you're asking about: '{user_input}'. As an AI assistant, I'm designed to help with any topic. Could you please provide more details so I can give you a comprehensive answer?"
    
    def clear_history(self):
        """"""Clear conversation history""""""
        self.conversation_history = []
        self.logger.info("Conversation history cleared")
    
    def export_conversation(self, filepath: str):
        """"""
        Export conversation history to file
        
        Args:
            filepath: Path to export file
        """"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            self.logger.info(f"Conversation exported to {filepath}")
        except Exception as e:
            self.logger.error(f"Failed to export conversation: {e}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """"""
        Get conversation statistics
        
        Returns:
            Statistics dictionary
        """"""
        languages_used = set(msg.get('language', 'unknown') for msg in self.conversation_history)
        
        return {
            'total_messages': len(self.conversation_history),
            'languages_used': list(languages_used),
            'current_language': self.current_language,
            'user_messages': len([m for m in self.conversation_history if m['role'] == 'user']),
            'assistant_messages': len([m for m in self.conversation_history if m['role'] == 'assistant'])
        }

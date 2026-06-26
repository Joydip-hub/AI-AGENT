"""
AI-AGENT - Smooth Multilingual Chatbot
Easy to download, install, and use!
"""

import sys
import os
import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
import uuid

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

class SmoothAIAgent:
    """
    Streamlined AI Agent for smooth user experience
    """
    
    def __init__(self):
        """Initialize the smooth AI agent"""
        self.conversation_history = []
        self.current_language = 'en'
        self.session_id = f"session_{uuid.uuid4().hex[:8]}"
        
        # Simple language patterns for detection
        self.language_patterns = {
            'hi': ['namaste', 'kaise', 'kya', 'hai', 'main', 'aap', 'tum'],
            'es': ['hola', 'como', 'que', 'buenos', 'dias', 'gracias'],
            'fr': ['bonjour', 'comment', 'merci', 'oui', 'non', 'je'],
            'de': ['hallo', 'wie', 'was', 'danke', 'ja', 'nein'],
            'zh': ['ni', 'hao', 'shi', 'bu', 'xie', 'zai'],
            'ja': ['konnichiwa', 'arigatou', 'hai', 'ie', 'desu'],
            'ar': ['marhaba', 'shukran', 'naam', 'la', 'min'],
            'ta': ['vanakkam', 'nandri', 'aamaa', 'illai', 'naan'],
            'te': ['namaskaram', 'dhanyavaadalu', 'avunu', 'kaadu'],
            'pt': ['ola', 'obrigado', 'sim', 'nao', 'eu'],
            'ru': ['privet', 'spasibo', 'da', 'net', 'ya']
        }
        
        print("✓ AI Agent initialized successfully!")
    
    def detect_language(self, text: str) -> str:
        """Detect language from text"""
        text_lower = text.lower()
        
        for lang, patterns in self.language_patterns.items():
            if any(pattern in text_lower for pattern in patterns):
                return lang
        
        return 'en'
    
    def generate_response(self, user_input: str) -> Dict[str, Any]:
        """Generate smooth, intelligent response"""
        # Detect language
        detected_lang = self.detect_language(user_input)
        self.current_language = detected_lang
        
        # Add to history
        self.conversation_history.append({
            'role': 'user',
            'content': user_input,
            'language': detected_lang,
            'timestamp': datetime.now().isoformat()
        })
        
        # Generate contextual response
        response = self._create_response(user_input, detected_lang)
        
        # Add response to history
        self.conversation_history.append({
            'role': 'assistant',
            'content': response,
            'language': detected_lang,
            'timestamp': datetime.now().isoformat()
        })
        
        return {
            'content': response,
            'language': detected_lang,
            'session_id': self.session_id
        }
    
    def _create_response(self, user_input: str, language: str) -> str:
        """Create intelligent response based on input"""
        input_lower = user_input.lower()
        
        # Greeting responses
        greetings = {
            'en': "Hello! I'm your AI assistant. How can I help you today?",
            'hi': "नमस्ते! मैं आपका AI सहायक हूं। आज मैं आपकी कैसे मदद कर सकता हूं?",
            'es': "¡Hola! Soy tu asistente de IA. ¿Cómo puedo ayudarte hoy?",
            'fr': "Bonjour! Je suis votre assistant IA. Comment puis-je vous aider aujourd'hui?",
            'de': "Hallo! Ich bin dein KI-Assistent. Wie kann ich dir heute helfen?",
            'zh': "你好！我是您的AI助手。今天我能帮您什么？",
            'ja': "こんにちは！私はあなたのAIアシスタントです。今日はどのようにお手伝いできますか？",
            'ar': "مرحبا! أنا مساعدك الذكي. كيف يمكنني مساعدتك اليوم؟",
            'ta': "வணக்கம்! நான் உங்கள் AI உதவியாளர். இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?",
            'te': "నమస్కారం! నేను మీ AI సహాయకుడిని. ఈ రోజు నేను మీకు ఎలా సహాయం చేయగలను?",
            'pt': "Olá! Sou seu assistente de IA. Como posso ajudá-lo hoje?",
            'ru': "Привет! Я ваш ИИ-ассистент. Чем я могу помочь вам сегодня?"
        }
        
        # Check for greetings
        greeting_words = ['hello', 'hi', 'hey', 'namaste', 'hola', 'bonjour', 'hallo', 
                         'ni hao', 'konnichiwa', 'marhaba', 'vanakkam', 'namaskaram']
        
        if any(word in input_lower for word in greeting_words):
            return greetings.get(language, greetings['en'])
        
        # Topic-based responses
        if any(word in input_lower for word in ['weather', 'climate', 'temperature']):
            return self._get_weather_response(language)
        
        if any(word in input_lower for word in ['time', 'date', 'day']):
            return self._get_time_response(language)
        
        if any(word in input_lower for word in ['help', 'support', 'assist']):
            return self._get_help_response(language)
        
        if any(word in input_lower for word in ['thank', 'thanks', 'shukriya']):
            return self._get_thanks_response(language)
        
        # Default intelligent response
        return self._get_default_response(user_input, language)
    
    def _get_weather_response(self, language: str) -> str:
        """Weather-related response"""
        responses = {
            'en': "I'd be happy to help with weather information! For accurate weather data, you can check weather.com or use a weather app. Is there a specific location you're interested in?",
            'hi': "मौसम की जानकारी में मदद करके खुशी होगी! सटीक मौसम डेटा के लिए, आप weather.com देख सकते हैं या मौसम ऐप का उपयोग कर सकते हैं।",
            'es': "¡Estaré encantado de ayudar con información del clima! Para datos meteorológicos precisos, puedes consultar weather.com o usar una app del clima.",
            'fr': "Je serais ravi de vous aider avec les informations météo! Pour des données météorologiques précises, vous pouvez consulter weather.com ou utiliser une application météo."
        }
        return responses.get(language, responses['en'])
    
    def _get_time_response(self, language: str) -> str:
        """Time-related response"""
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        responses = {
            'en': f"The current time is {current_time} and today's date is {current_date}.",
            'hi': f"वर्तमान समय {current_time} है और आज की तारीख {current_date} है।",
            'es': f"La hora actual es {current_time} y la fecha de hoy es {current_date}.",
            'fr': f"L'heure actuelle est {current_time} et la date d'aujourd'hui est {current_date}."
        }
        return responses.get(language, responses['en'])
    
    def _get_help_response(self, language: str) -> str:
        """Help response"""
        responses = {
            'en': "I'm here to help! You can ask me about:\n- General knowledge and information\n- Weather and time\n- Language translation\n- Daily assistance\n- And much more! Just ask me anything.",
            'hi': "मैं मदद के लिए यहां हूं! आप मुझसे पूछ सकते हैं:\n- सामान्य ज्ञान और जानकारी\n- मौसम और समय\n- भाषा अनुवाद\n- दैनिक सहायता\n- और बहुत कुछ! बस मुझसे कुछ भी पूछें।",
            'es': "¡Estoy aquí para ayudar! Puedes preguntarme sobre:\n- Conocimiento general e información\n- Clima y hora\n- Traducción de idiomas\n- Asistencia diaria\n- ¡Y mucho más! Solo pregúntame lo que quieras.",
            'fr': "Je suis là pour vous aider! Vous pouvez me demander:\n- Connaissances générales et informations\n- Météo et heure\n- Traduction linguistique\n- Assistance quotidienne\n- Et bien plus encore! Demandez-moi n'importe quoi."
        }
        return responses.get(language, responses['en'])
    
    def _get_thanks_response(self, language: str) -> str:
        """Thanks response"""
        responses = {
            'en': "You're welcome! I'm glad I could help. Is there anything else you'd like to know?",
            'hi': "आपका स्वागत है! मुझे खुशी है कि मैं मदद कर सका। क्या कुछ और है जो आप जानना चाहेंगे?",
            'es': "¡De nada! Me alegra haber podido ayudar. ¿Hay algo más que te gustaría saber?",
            'fr': "De rien! Je suis content d'avoir pu aider. Y a-t-il autre chose que vous aimeriez savoir?"
        }
        return responses.get(language, responses['en'])
    
    def _get_default_response(self, user_input: str, language: str) -> str:
        """Default intelligent response"""
        responses = {
            'en': f"I understand you're asking about: '{user_input}'. I'm designed to help with any topic. Could you please provide more details so I can give you a comprehensive answer?",
            'hi': f"मैं समझता हूं कि आप '{user_input}' के बारे में पूछ रहे हैं। मैं किसी भी विषय पर मदद करने के लिए डिज़ाइन किया गया हूं। कृपया अधिक विवरण दें ताकि मैं आपको व्यापक उत्तर दे सकूं।",
            'es': f"Entiendo que estás preguntando sobre: '{user_input}'. Estoy diseñado para ayudar con cualquier tema. ¿Podrías proporcionar más detalles para que pueda darte una respuesta completa?",
            'fr': f"Je comprends que vous demandez: '{user_input}'. Je suis conçu pour aider sur n'importe quel sujet. Pourriez-vous fournir plus de détails afin que je puisse vous donner une réponse complète?"
        }
        return responses.get(language, responses['en'])
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get conversation statistics"""
        languages_used = set(msg.get('language', 'unknown') for msg in self.conversation_history)
        
        return {
            'total_messages': len(self.conversation_history),
            'languages_used': list(languages_used),
            'current_language': self.current_language,
            'session_id': self.session_id,
            'user_messages': len([m for m in self.conversation_history if m['role'] == 'user']),
            'assistant_messages': len([m for m in self.conversation_history if m['role'] == 'assistant'])
        }
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("✓ Conversation history cleared!")
    
    def export_conversation(self, filepath: str):
        """Export conversation to file"""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            print(f"✓ Conversation exported to {filepath}")
        except Exception as e:
            print(f"✗ Failed to export: {e}")

# Make it easy to import
AIAgent = SmoothAIAgent

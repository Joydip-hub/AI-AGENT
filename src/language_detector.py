"""
Language Detection Module for AI Chatbot
Supports detection of multiple languages including regional variants
"""

from langdetect import detect, detect_langs
from typing import Dict, List, Optional
import logging

class LanguageDetector:
    """
    Detects and manages multiple language support for the chatbot
    """
    
    # Comprehensive language mapping including regional languages
    SUPPORTED_LANGUAGES = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'zh-cn': 'Chinese (Simplified)',
        'zh-tw': 'Chinese (Traditional)',
        'ja': 'Japanese',
        'ko': 'Korean',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'bn': 'Bengali',
        'pa': 'Punjabi',
        'te': 'Telugu',
        'mr': 'Marathi',
        'ta': 'Tamil',
        'ur': 'Urdu',
        'gu': 'Gujarati',
        'kn': 'Kannada',
        'ml': 'Malayalam',
        'or': 'Odia',
        'th': 'Thai',
        'vi': 'Vietnamese',
        'id': 'Indonesian',
        'ms': 'Malay',
        'fil': 'Filipino',
        'tr': 'Turkish',
        'pl': 'Polish',
        'uk': 'Ukrainian',
        'ro': 'Romanian',
        'nl': 'Dutch',
        'sv': 'Swedish',
        'da': 'Danish',
        'no': 'Norwegian',
        'fi': 'Finnish',
        'cs': 'Czech',
        'el': 'Greek',
        'he': 'Hebrew',
        'fa': 'Persian',
        'sw': 'Swahili',
        'am': 'Amharic',
        'ne': 'Nepali',
        'si': 'Sinhala',
        'my': 'Burmese',
        'km': 'Khmer',
        'lo': 'Lao'
    }
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.default_language = 'en'
    
    def detect_language(self, text: str) -> str:
        """
        Detect the language of given text
        
        Args:
            text: Input text to detect language
            
        Returns:
            Language code (e.g., 'en', 'hi', 'es')
        """
        try:
            if not text or len(text.strip()) < 3:
                return self.default_language
            
            detected = detect(text)
            return detected
        except Exception as e:
            self.logger.warning(f"Language detection failed: {e}")
            return self.default_language
    
    def detect_language_probability(self, text: str) -> List[Dict[str, float]]:
        """
        Detect language with probability scores
        
        Args:
            text: Input text
            
        Returns:
            List of detected languages with probabilities
        """
        try:
            if not text or len(text.strip()) < 3:
                return [{'lang': self.default_language, 'prob': 1.0}]
            
            detected_langs = detect_langs(text)
            return [{'lang': lang.lang, 'prob': lang.prob} for lang in detected_langs]
        except Exception as e:
            self.logger.warning(f"Language probability detection failed: {e}")
            return [{'lang': self.default_language, 'prob': 1.0}]
    
    def get_language_name(self, lang_code: str) -> str:
        """
        Get full language name from code
        
        Args:
            lang_code: Language code (e.g., 'en')
            
        Returns:
            Full language name (e.g., 'English')
        """
        return self.SUPPORTED_LANGUAGES.get(lang_code, 'Unknown')
    
    def is_supported(self, lang_code: str) -> bool:
        """
        Check if language is supported
        
        Args:
            lang_code: Language code
            
        Returns:
            True if supported, False otherwise
        """
        return lang_code in self.SUPPORTED_LANGUAGES
    
    def get_all_supported_languages(self) -> Dict[str, str]:
        """
        Get all supported languages
        
        Returns:
            Dictionary of language codes and names
        """
        return self.SUPPORTED_LANGUAGES.copy()

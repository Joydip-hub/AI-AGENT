"""
__init__.py for src package
"""

from .ai_agent import AIAgent
from .language_detector import LanguageDetector
from .conversation_manager import ConversationManager
from .knowledge_base import KnowledgeBase

__version__ = "1.0.0"
__all__ = ['AIAgent', 'LanguageDetector', 'ConversationManager', 'KnowledgeBase']

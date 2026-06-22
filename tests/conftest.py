"""
Test configuration and fixtures
"""

import pytest
import sys
import os

# Add src to path for tests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

@pytest.fixture
def sample_agent():
    """Create a sample AI agent for testing"""
    from ai_agent import AIAgent
    return AIAgent()

@pytest.fixture
def sample_conversation_manager():
    """Create a sample conversation manager for testing"""
    from conversation_manager import ConversationManager
    return ConversationManager(storage_path="./test_data")

@pytest.fixture
def sample_language_detector():
    """Create a sample language detector for testing"""
    from language_detector import LanguageDetector
    return LanguageDetector()

@pytest.fixture
def sample_knowledge_base():
    """Create a sample knowledge base for testing"""
    from knowledge_base import KnowledgeBase
    return KnowledgeBase()

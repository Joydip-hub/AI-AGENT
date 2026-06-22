"""
Unit Tests for AI Agent
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from ai_agent import AIAgent
from conversation_manager import ConversationManager
from language_detector import LanguageDetector
from knowledge_base import KnowledgeBase

class TestAIAgent:
    """Test cases for AIAgent class"""
    
    def test_agent_initialization(self):
        """Test agent initialization"""
        agent = AIAgent()
        assert agent is not None
        assert agent.conversation_history == []
        assert agent.current_language == 'en'
    
    def test_process_input(self):
        """Test processing user input"""
        agent = AIAgent()
        response = agent.process_input("Hello")
        
        assert response is not None
        assert 'content' in response
        assert 'language' in response
        assert 'timestamp' in response
    
    def test_conversation_history(self):
        """Test conversation history tracking"""
        agent = AIAgent()
        
        agent.process_input("Hello")
        agent.process_input("How are you?")
        
        assert len(agent.conversation_history) == 4  # 2 user + 2 assistant
    
    def test_clear_history(self):
        """Test clearing conversation history"""
        agent = AIAgent()
        
        agent.process_input("Hello")
        agent.clear_history()
        
        assert len(agent.conversation_history) == 0
    
    def test_statistics(self):
        """Test getting statistics"""
        agent = AIAgent()
        
        agent.process_input("Hello")
        stats = agent.get_statistics()
        
        assert stats['total_messages'] == 2
        assert stats['user_messages'] == 1
        assert stats['assistant_messages'] == 1

class TestLanguageDetector:
    """Test cases for LanguageDetector class"""
    
    def test_detector_initialization(self):
        """Test language detector initialization"""
        detector = LanguageDetector()
        assert detector is not None
        assert detector.default_language == 'en'
    
    def test_language_detection(self):
        """Test language detection"""
        detector = LanguageDetector()
        
        # Test English
        lang = detector.detect_language("This is English")
        assert lang == 'en'
        
        # Test Spanish
        lang = detector.detect_language("Esto es español")
        assert lang == 'es'
    
    def test_supported_languages(self):
        """Test supported languages"""
        detector = LanguageDetector()
        langs = detector.get_all_supported_languages()
        
        assert 'en' in langs
        assert 'hi' in langs
        assert 'es' in langs

class TestConversationManager:
    """Test cases for ConversationManager class"""
    
    def test_create_session(self):
        """Test session creation"""
        manager = ConversationManager()
        session = manager.create_session("test_session")
        
        assert session is not None
        assert session['session_id'] == "test_session"
        assert len(session['messages']) == 0
    
    def test_add_message(self):
        """Test adding messages"""
        manager = ConversationManager()
        manager.create_session("test_session")
        
        manager.add_message("test_session", "user", "Hello")
        session = manager.get_session("test_session")
        
        assert len(session['messages']) == 1
        assert session['messages'][0]['role'] == 'user'
    
    def test_get_context(self):
        """Test getting conversation context"""
        manager = ConversationManager()
        manager.create_session("test_session")
        
        manager.add_message("test_session", "user", "Hello")
        manager.add_message("test_session", "assistant", "Hi there")
        
        context = manager.get_context("test_session", limit=2)
        assert len(context) == 2

class TestKnowledgeBase:
    """Test cases for KnowledgeBase class"""
    
    def test_knowledge_base_initialization(self):
        """Test knowledge base initialization"""
        kb = KnowledgeBase()
        assert kb is not None
    
    def test_get_categories(self):
        """Test getting categories"""
        kb = KnowledgeBase()
        categories = kb.get_all_categories()
        
        assert 'science' in categories
        assert 'technology' in categories
        assert 'mathematics' in categories
    
    def test_search_knowledge(self):
        """Test searching knowledge"""
        kb = KnowledgeBase()
        results = kb.search_knowledge("physics")
        
        assert results is not None
    
    def test_get_category(self):
        """Test getting specific category"""
        kb = KnowledgeBase()
        science = kb.get_category('science')
        
        assert science is not None
        assert 'physics' in science

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

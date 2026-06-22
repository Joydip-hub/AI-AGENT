"""
Example Usage Script for AI-AGENT
Demonstrates various features of the multilingual AI chatbot
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ai_agent import AIAgent
from conversation_manager import ConversationManager
from language_detector import LanguageDetector
from knowledge_base import KnowledgeBase

def example_basic_conversation():
    """Example: Basic conversation with the AI agent"""
    print("\n=== Example 1: Basic Conversation ===\n")
    
    agent = AIAgent()
    
    # English conversation
    response = agent.process_input("Hello! How are you?")
    print(f"User: Hello! How are you?")
    print(f"Agent: {response['content']}\n")
    
    # Follow-up question
    response = agent.process_input("What can you help me with?")
    print(f"User: What can you help me with?")
    print(f"Agent: {response['content']}\n")

def example_multilingual():
    """Example: Multilingual conversation"""
    print("\n=== Example 2: Multilingual Conversation ===\n")
    
    agent = AIAgent()
    
    examples = [
        ("Hello!", "English"),
        ("¡Hola!", "Spanish"),
        ("Bonjour!", "French"),
        ("नमस्ते!", "Hindi"),
        ("你好!", "Chinese"),
        ("こんにちは!", "Japanese"),
        ("مرحبا!", "Arabic"),
        ("வணக்கம்!", "Tamil")
    ]
    
    for text, lang_name in examples:
        response = agent.process_input(text)
        print(f"[{lang_name}] User: {text}")
        print(f"[{lang_name}] Agent: {response['content'][:100]}...")
        print(f"Detected Language: {response['language']}\n")

def example_conversation_management():
    """Example: Using conversation manager"""
    print("\n=== Example 3: Conversation Management ===\n")
    
    conv_manager = ConversationManager()
    agent = AIAgent()
    
    # Create session
    session_id = "demo_session_001"
    conv_manager.create_session(session_id, user_info={'name': 'Demo User'})
    print(f"Created session: {session_id}\n")
    
    # Have a conversation
    messages = [
        "What is artificial intelligence?",
        "How is it used in everyday life?",
        "What are the benefits?"
    ]
    
    for msg in messages:
        response = agent.process_input(msg)
        
        # Add to conversation manager
        conv_manager.add_message(session_id, 'user', msg)
        conv_manager.add_message(session_id, 'assistant', response['content'])
        
        print(f"User: {msg}")
        print(f"Agent: {response['content'][:150]}...\n")
    
    # Get statistics
    stats = conv_manager.get_session_stats(session_id)
    print(f"Session Statistics:")
    print(f"  Total messages: {stats['total_messages']}")
    print(f"  User messages: {stats['user_messages']}")
    print(f"  Assistant messages: {stats['assistant_messages']}")
    print(f"  Duration: {stats['duration_minutes']} minutes\n")
    
    # Save session
    conv_manager.save_session(session_id)
    print(f"Session saved to disk\n")

def example_language_detection():
    """Example: Language detection"""
    print("\n=== Example 4: Language Detection ===\n")
    
    detector = LanguageDetector()
    
    texts = [
        "This is an English sentence.",
        "Esto es una oración en español.",
        "यह हिंदी में एक वाक्य है।",
        "これは日本語の文です。",
        "هذه جملة باللغة العربية.",
        "இது தமிழில் ஒரு வாக்கியம்."
    ]
    
    for text in texts:
        lang = detector.detect_language(text)
        lang_name = detector.get_language_name(lang)
        probs = detector.detect_language_probability(text)
        
        print(f"Text: {text}")
        print(f"Detected: {lang_name} ({lang})")
        print(f"Confidence: {probs[0]['prob']:.2%}\n")

def example_knowledge_base():
    """Example: Using knowledge base"""
    print("\n=== Example 5: Knowledge Base Usage ===\n")
    
    kb = KnowledgeBase()
    
    # Get all categories
    categories = kb.get_all_categories()
    print(f"Available categories: {', '.join(categories)}\n")
    
    # Search for information
    query = "artificial intelligence"
    results = kb.search_knowledge(query)
    print(f"Search results for '{query}':")
    if results:
        for category, content in results.items():
            print(f"  Category: {category}")
            print(f"  Content: {content}\n")
    
    # Get specific category
    science = kb.get_category('science')
    print("Science category:")
    for key, value in science.items():
        print(f"  {key}: {value}")

def example_statistics():
    """Example: Getting conversation statistics"""
    print("\n=== Example 6: Conversation Statistics ===\n")
    
    agent = AIAgent()
    
    # Have some conversations
    conversations = [
        "Hello!",
        "¿Cómo estás?",
        "Bonjour!",
        "What is Python?",
        "नमस्ते!"
    ]
    
    for msg in conversations:
        agent.process_input(msg)
    
    # Get statistics
    stats = agent.get_statistics()
    print("Conversation Statistics:")
    print(f"  Total messages: {stats['total_messages']}")
    print(f"  User messages: {stats['user_messages']}")
    print(f"  Assistant messages: {stats['assistant_messages']}")
    print(f"  Languages used: {', '.join(stats['languages_used'])}")
    print(f"  Current language: {stats['current_language']}\n")

def example_export_conversation():
    """Example: Exporting conversation"""
    print("\n=== Example 7: Export Conversation ===\n")
    
    agent = AIAgent()
    
    # Have a conversation
    agent.process_input("Hello!")
    agent.process_input("What is machine learning?")
    agent.process_input("Thank you!")
    
    # Export to file
    export_path = "../data/example_export.json"
    agent.export_conversation(export_path)
    print(f"Conversation exported to: {export_path}\n")

def main():
    """Run all examples"""
    print("=" * 60)
    print("AI-AGENT Example Usage Demonstrations")
    print("=" * 60)
    
    try:
        example_basic_conversation()
        example_multilingual()
        example_conversation_management()
        example_language_detection()
        example_knowledge_base()
        example_statistics()
        example_export_conversation()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

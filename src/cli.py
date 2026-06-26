"""
CLI Module for AI-AGENT Terminal Command
Enables running chatbot directly from terminal after pip install
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from ai_agent import AIAgent
from conversation_manager import ConversationManager
import uuid

def print_banner():
    """Print welcome banner"""
    print("=" * 60)
    print("   AI-AGENT: Multilingual AI Chatbot")
    print("   Type in any language and I'll respond!")
    print("=" * 60)
    print()

def print_help():
    """Print help information"""
    print("\nAvailable Commands:")
    print("  help       - Show this help message")
    print("  stats      - Show conversation statistics")
    print("  clear      - Clear conversation history")
    print("  export     - Export conversation to file")
    print("  lang       - Show detected language")
    print("  quit       - Exit the chatbot")
    print()

def main():
    """
    Main CLI function for advanced mode
    Run with: ai-agent
    """
    print_banner()
    
    # Initialize components
    agent = AIAgent()
    conv_manager = ConversationManager()
    session_id = f"session_{uuid.uuid4().hex[:8]}"
    
    # Create session
    conv_manager.create_session(session_id)
    
    print("Chatbot ready! Type 'help' for commands or start chatting.")
    print("You can type in any language!\n")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['/quit', '/exit', 'quit', 'exit']:
                print("\nThank you for using AI-AGENT! Goodbye!")
                conv_manager.save_session(session_id)
                break
            
            elif user_input.lower() in ['/help', 'help']:
                print_help()
                continue
            
            elif user_input.lower() in ['/stats', 'stats']:
                stats = agent.get_statistics()
                session_stats = conv_manager.get_session_stats(session_id)
                print("\n--- Conversation Statistics ---")
                print(f"Total messages: {stats['total_messages']}")
                print(f"Languages used: {', '.join(stats['languages_used'])}")
                print(f"Session duration: {session_stats['duration_minutes']} minutes")
                print()
                continue
            
            elif user_input.lower() in ['/clear', 'clear']:
                agent.clear_history()
                print("Conversation history cleared!\n")
                continue
            
            elif user_input.lower() in ['/export', 'export']:
                filename = f"conversation_{session_id}.json"
                agent.export_conversation(f"./data/{filename}")
                print(f"Conversation exported to ./data/{filename}\n")
                continue
            
            elif user_input.lower() in ['/lang', 'lang']:
                print(f"Current detected language: {agent.current_language}")
                if agent.language_detector:
                    lang_name = agent.language_detector.get_language_name(agent.current_language)
                    print(f"Language name: {lang_name}\n")
                continue
            
            # Process user input
            response = agent.process_input(user_input)
            
            # Add to conversation manager
            conv_manager.add_message(session_id, 'user', user_input, response['language'])
            conv_manager.add_message(session_id, 'assistant', response['content'], response['language'])
            
            # Display response
            print(f"Agent: {response['content']}")
            print()
        
        except KeyboardInterrupt:
            print("\n\nInterrupted! Saving session...")
            conv_manager.save_session(session_id)
            print("Goodbye!")
            break
        
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again or type 'help' for assistance\n")

def simple_main():
    """
    Simple CLI function for basic mode
    Run with: ai-agent-simple
    """
    print("=" * 60)
    print("   AI-AGENT: Multilingual AI Chatbot (Simple Mode)")
    print("   Type 'quit' to exit, 'help' for commands")
    print("=" * 60)
    print()
    
    agent = AIAgent()
    
    print("Chatbot ready! Start typing in any language...\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nGoodbye!")
                break
            
            if user_input.lower() == 'help':
                print("\nCommands:")
                print("  quit/exit - Exit the chatbot")
                print("  help - Show this help")
                print("  stats - Show statistics")
                print("  clear - Clear history\n")
                continue
            
            if user_input.lower() == 'stats':
                stats = agent.get_statistics()
                print(f"\nTotal messages: {stats['total_messages']}")
                print(f"Languages: {', '.join(stats['languages_used'])}\n")
                continue
            
            if user_input.lower() == 'clear':
                agent.clear_history()
                print("\nHistory cleared!\n")
                continue
            
            response = agent.process_input(user_input)
            print(f"Agent: {response['content']}\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()

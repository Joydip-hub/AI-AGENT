"""
Main Entry Point for AI-AGENT Chatbot
Run this file to start the interactive chatbot
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ai_agent import AIAgent
from conversation_manager import ConversationManager
from colorama import init, Fore, Style
import uuid

# Initialize colorama for colored terminal output
init(autoreset=True)

def print_banner():
    """Print welcome banner"""
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "   AI-AGENT: Multilingual AI Chatbot")
    print(Fore.CYAN + "   Supports 40+ languages including regional variants")
    print(Fore.CYAN + "=" * 60)
    print()

def print_help():
    """Print help information"""
    print(Fore.YELLOW + "\nAvailable Commands:")
    print(Fore.GREEN + "  /help" + Fore.WHITE + "       - Show this help message")
    print(Fore.GREEN + "  /stats" + Fore.WHITE + "      - Show conversation statistics")
    print(Fore.GREEN + "  /clear" + Fore.WHITE + "      - Clear conversation history")
    print(Fore.GREEN + "  /export" + Fore.WHITE + "     - Export conversation to file")
    print(Fore.GREEN + "  /lang" + Fore.WHITE + "       - Show detected language")
    print(Fore.GREEN + "  /quit" + Fore.WHITE + "       - Exit the chatbot")
    print()

def main():
    """Main function to run the chatbot"""
    print_banner()
    
    # Initialize components
    agent = AIAgent()
    conv_manager = ConversationManager()
    session_id = f"session_{uuid.uuid4().hex[:8]}"
    
    # Create session
    conv_manager.create_session(session_id)
    
    print(Fore.GREEN + "Chatbot initialized! Type '/help' for commands or start chatting.")
    print(Fore.YELLOW + "You can type in any language, and I'll respond accordingly!\n")
    
    while True:
        try:
            # Get user input
            user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL).strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.startswith('/'):
                command = user_input.lower()
                
                if command == '/quit' or command == '/exit':
                    print(Fore.YELLOW + "\nThank you for using AI-AGENT! Goodbye!")
                    conv_manager.save_session(session_id)
                    break
                
                elif command == '/help':
                    print_help()
                    continue
                
                elif command == '/stats':
                    stats = agent.get_statistics()
                    session_stats = conv_manager.get_session_stats(session_id)
                    print(Fore.CYAN + "\n--- Conversation Statistics ---")
                    print(Fore.WHITE + f"Total messages: {stats['total_messages']}")
                    print(Fore.WHITE + f"Languages used: {', '.join(stats['languages_used'])}")
                    print(Fore.WHITE + f"Session duration: {session_stats['duration_minutes']} minutes")
                    print()
                    continue
                
                elif command == '/clear':
                    agent.clear_history()
                    print(Fore.YELLOW + "Conversation history cleared!\n")
                    continue
                
                elif command == '/export':
                    filename = f"conversation_{session_id}.json"
                    agent.export_conversation(f"./data/{filename}")
                    print(Fore.GREEN + f"Conversation exported to ./data/{filename}\n")
                    continue
                
                elif command == '/lang':
                    print(Fore.CYAN + f"Current detected language: {agent.current_language}")
                    if agent.language_detector:
                        lang_name = agent.language_detector.get_language_name(agent.current_language)
                        print(Fore.CYAN + f"Language name: {lang_name}\n")
                    continue
                
                else:
                    print(Fore.RED + f"Unknown command: {user_input}")
                    print(Fore.YELLOW + "Type '/help' for available commands\n")
                    continue
            
            # Process user input
            response = agent.process_input(user_input)
            
            # Add to conversation manager
            conv_manager.add_message(session_id, 'user', user_input, response['language'])
            conv_manager.add_message(session_id, 'assistant', response['content'], response['language'])
            
            # Display response
            print(Fore.GREEN + "Agent: " + Style.RESET_ALL + response['content'])
            print()
        
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\nInterrupted! Saving session...")
            conv_manager.save_session(session_id)
            print(Fore.YELLOW + "Goodbye!")
            break
        
        except Exception as e:
            print(Fore.RED + f"\nError: {e}")
            print(Fore.YELLOW + "Please try again or type '/help' for assistance\n")

if __name__ == "__main__":
    main()

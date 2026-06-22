"""
Simple CLI Chatbot Interface
A simpler alternative to main.py without external dependencies
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ai_agent import AIAgent

def main():
    """Simple CLI chatbot"""
    print("=" * 60)
    print("   AI-AGENT: Multilingual AI Chatbot")
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

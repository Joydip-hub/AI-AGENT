#!/usr/bin/env python3
"""
AI-AGENT - Simple & Smooth Chatbot
Easy to download and use!
"""

import sys
import os
import time

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_banner():
    """Print beautiful banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║            🤖 AI-AGENT - Smooth Multilingual Chatbot         ║
║                                                              ║
║       Converse naturally in 40+ languages with ease!         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_help():
    """Print help information"""
    help_text = """
┌─────────────────────────────────────────────────────────────┐
│                    📋 AVAILABLE COMMANDS                     │
├─────────────────────────────────────────────────────────────┤
│  help     - Show this help message                          │
│  stats    - View conversation statistics                    │
│  clear    - Clear conversation history                      │
│  export   - Save conversation to file                       │
│  quit     - Exit the chatbot                                │
└─────────────────────────────────────────────────────────────┘

💡 Tips:
• Type in any language - I'll detect and respond accordingly!
• Ask about weather, time, general knowledge, or just chat!
• I support English, Hindi, Spanish, French, and many more!
    """
    print(help_text)

def print_welcome():
    """Print welcome message"""
    welcome = """
🌟 Welcome to AI-AGENT! 

I'm your multilingual AI assistant. I can:
• Understand and respond in 40+ languages
• Help with various topics
• Remember our conversation
• Provide smooth, natural responses

Just start typing to begin our conversation!
    """
    print_slow(welcome)

def main():
    """Main chatbot function"""
    try:
        # Import the smooth agent
        from smooth_agent import SmoothAIAgent
        
        clear_screen()
        print_banner()
        print_welcome()
        
        # Initialize agent
        print("🔄 Initializing AI Agent...")
        agent = SmoothAIAgent()
        print()
        
        # Main conversation loop
        while True:
            try:
                # Get user input with nice prompt
                user_input = input("\033[1;34m💬 You: \033[0m").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                    farewell = "\n👋 Thank you for using AI-AGENT! Goodbye!\n"
                    print_slow(farewell)
                    break
                
                if user_input.lower() == 'help':
                    print_help()
                    continue
                
                if user_input.lower() == 'stats':
                    stats = agent.get_statistics()
                    print(f"\n📊 Conversation Statistics:")
                    print(f"   Total messages: {stats['total_messages']}")
                    print(f"   Languages used: {', '.join(stats['languages_used'])}")
                    print(f"   Session ID: {stats['session_id']}")
                    continue
                
                if user_input.lower() == 'clear':
                    agent.clear_history()
                    continue
                
                if user_input.lower() == 'export':
                    filename = f"conversation_{agent.session_id}.json"
                    agent.export_conversation(f"./data/{filename}")
                    continue
                
                # Process input and get response
                print("\n🤖 AI Agent: ", end="")
                response = agent.generate_response(user_input)
                
                # Print response with typing effect
                print_slow(response['content'], delay=0.02)
                
                # Show detected language
                lang = response['language']
                if lang != 'en':
                    print(f"   [Language detected: {lang}]")
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted! Type 'quit' to exit properly.")
                continue
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("   Please try again or type 'help' for assistance.")
                continue
    
    except ImportError as e:
        print(f"❌ Error: Could not import required modules.")
        print(f"   Please run: pip install -r requirements.txt")
        print(f"   Error details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

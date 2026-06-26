"""
AI-AGENT - Your AI Friend!
Super simple, super fast!
"""

import os
import sys
import time
from datetime import datetime

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Try to import colorama
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except:
    # If colorama not installed, use empty strings
    class Fore:
        CYAN = ""
        GREEN = ""
        YELLOW = ""
        RED = ""
        BLUE = ""
    class Style:
        RESET_ALL = ""

# Try to import langdetect
try:
    from langdetect import detect
    HAS_LANG = True
except:
    HAS_LANG = False

def detect_language(text):
    """Detect language from text"""
    if HAS_LANG:
        try:
            return detect(text)
        except:
            pass
    
    # Simple detection based on characters
    for char in text:
        if '\u0900' <= char <= '\u097F':
            return 'hi'
        if '\u4E00' <= char <= '\u9FFF':
            return 'zh'
        if '\u3040' <= char <= '\u309F':
            return 'ja'
        if '\u0600' <= char <= '\u06FF':
            return 'ar'
        if '\u0B80' <= char <= '\u0BFF':
            return 'ta'
        if '\u0C00' <= char <= '\u0C7F':
            return 'te'
    
    return 'en'

def get_response(text):
    """Get response based on input"""
    text_lower = text.lower().strip()
    lang = detect_language(text)
    
    # Greetings
    greetings = ['hello', 'hi', 'hey', 'hola', 'bonjour', 'hallo', 'ciao', 'namaste', 'yo']
    if any(g in text_lower for g in greetings):
        responses = {
            'en': "Hey there! I'm your AI friend! What's up?",
            'hi': "नमस्ते! मैं आपका AI दोस्त हूं!",
            'es': "¡Hola! ¡Soy tu amigo AI!",
            'fr': "Salut! Je suis ton ami AI!",
            'de': "Hallo! Ich bin dein AI-Freund!",
            'zh': "你好！我是你的AI朋友！",
            'ja': "やあ！僕はあなたのAI友達だよ！",
            'ar': "مرحبا! أنا صديقك الذكي!",
            'ta': "வணக்கம்! நான் உங்கள் AI நண்பன்!",
            'te': "హాయ్! నేను మీ AI స్నేహితుడిని!",
        }
        return responses.get(lang, responses['en'])
    
    # How are you
    if 'how are you' in text_lower or 'how r u' in text_lower:
        responses = {
            'en': "I'm doing great! Thanks for asking! How about you?",
            'hi': "मैं बहुत अच्छा हूं! धन्यवाद!",
            'es': "¡Estoy muy bien! ¡Gracias!",
            'fr': "Je vais très bien! Merci!",
        }
        return responses.get(lang, responses['en'])
    
    # Bye
    if any(g in text_lower for g in ['bye', 'goodbye', 'see you']):
        responses = {
            'en': "Goodbye! Have an awesome day!",
            'hi': "अलविदा! आपका दिन शानदार हो!",
            'es': "¡Adiós! ¡Que tengas un día increíble!",
            'fr': "Au revoir! Passe une super journée!",
        }
        return responses.get(lang, responses['en'])
    
    # Thanks
    if 'thank' in text_lower:
        responses = {
            'en': "You're welcome! Happy to help!",
            'hi': "आपका स्वागत है!",
            'es': "¡De nada!",
            'fr': "De rien!",
        }
        return responses.get(lang, responses['en'])
    
    # Help
    if 'help' in text_lower:
        responses = {
            'en': "I can chat with you! Try:\n  - Hello\n  - How are you?\n  - Tell me a joke\n  - What time is it?\n  - Bye",
            'hi': "मैं आपसे बात कर सकता हूं!\n  - नमस्ते\n  - आप कैसे हैं?\n  - जोक सुनाओ\n  - कितने बजे हैं?",
        }
        return responses.get(lang, responses['en'])
    
    # Joke
    if 'joke' in text_lower or 'funny' in text_lower:
        return "Why don't scientists trust atoms? Because they make up everything! :D"
    
    # Time
    if 'time' in text_lower:
        current_time = datetime.now().strftime('%I:%M %p')
        return f"It's {current_time} right now!"
    
    # Name
    if 'name' in text_lower:
        return "I'm AI-AGENT, your friendly AI assistant!"
    
    # Love
    if 'love' in text_lower or 'awesome' in text_lower or 'cool' in text_lower:
        return "Aww, that's sweet! I love chatting with you too!"
    
    # Default response
    return f"I hear you! Tell me more about that!"

def print_slow(text, delay=0.02):
    """Print with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        if char in '.,!?':
            time.sleep(delay * 2)
        elif char == ' ':
            time.sleep(delay)
        else:
            time.sleep(delay * 0.5)
    print()

def clear_screen():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main chat function"""
    clear_screen()
    
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "   AI-AGENT - Your AI Friend!")
    print(Fore.CYAN + "=" * 50)
    print()
    print(Fore.GREEN + "Hi! I'm ready to chat!")
    print(Fore.YELLOW + "Type 'help' to see what I can do")
    print(Fore.YELLOW + "Type 'quit' to exit")
    print(Fore.CYAN + "=" * 50)
    print()
    
    while True:
        try:
            user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL).strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print()
                print_slow(Fore.YELLOW + "Bye bye! Have a great day!")
                print()
                break
            
            response = get_response(user_input)
            
            print()
            print(Fore.GREEN + "AI: ", end="")
            print_slow(response)
            print()
            
        except KeyboardInterrupt:
            print()
            print(Fore.YELLOW + "\nBye! See you next time!")
            break
        except Exception as e:
            print(Fore.RED + f"Oops! Error: {e}")

if __name__ == "__main__":
    main()

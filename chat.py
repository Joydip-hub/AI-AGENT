#!/usr/bin/env python3
"""
AI-AGENT - Your AI Friend!
Super simple, super fast!
Double-click this file to start chatting!
"""

import os
import sys
import time
import json
from datetime import datetime

# Fix encoding for Windows
if sys.platform == 'win32':
    import locale
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Try to import colorama for colors
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    class Fore:
        CYAN = ""
        GREEN = ""
        YELLOW = ""
        RED = ""
        BLUE = ""
        WHITE = ""
        MAGENTA = ""
    class Style:
        RESET_ALL = ""

# Try to import langdetect
try:
    from langdetect import detect
    LANG_DETECT = True
except ImportError:
    LANG_DETECT = False

# ============================================
# FAST RESPONSES - INSTANT REPLIES!
# ============================================

RESPONSES = {
    'hello': {
        'en': "Hey there! I'm your AI friend! What's up?",
        'hi': "नमस्ते! मैं आपका AI दोस्त हूं! क्या हाल है?",
        'es': "¡Hola! ¡Soy tu amigo AI! ¿Qué tal?",
        'fr': "Salut! Je suis ton ami AI! Comment ça va?",
        'de': "Hallo! Ich bin dein AI-Freund! Wie geht's?",
        'zh': "你好！我是你的AI朋友！你好吗？",
        'ja': "やあ！僕はあなたのAI友達だよ！元気？",
        'ar': "مرحبا! أنا صديقك الذكي! كيف حالك؟",
        'ta': "வணக்கம்! நான் உங்கள் AI நண்பன்! எப்படி இருக்கீங்க?",
        'te': "హాయ్! నేను మీ AI స్నేహితుడిని! ఎలా ఉన్నారు?",
        'pt': "Oi! Sou seu amigo AI! Tudo bem?",
        'ru': "Привет! Я твой AI друг! Как дела?"
    },
    'hi': {
        'en': "Hey! How are you doing today?",
        'hi': "अरे! आज आप कैसे हैं?",
        'es': "¡Ey! ¿Cómo estás hoy?",
        'fr': "Hey! Comment allez-vous aujourd'hui?",
        'de': "Hey! Wie geht es dir heute?"
    },
    'hey': {
        'en': "Hey hey! What can I do for you?",
        'hi': "अरे अरे! मैं आपके लिए क्या कर सकता हूं?",
        'es': "¡Ey ey! ¿Qué puedo hacer por ti?",
        'fr': "Hey hey! Que puis-je faire pour toi?"
    },
    'how are you': {
        'en': "I'm doing great! Thanks for asking! How about you?",
        'hi': "मैं बहुत अच्छा हूं! पूछने के लिए धन्यवाद! आप कैसे हैं?",
        'es': "¡Estoy muy bien! ¡Gracias por preguntar! ¿Y tú?",
        'fr': "Je vais très bien! Merci de demander! Et toi?"
    },
    'bye': {
        'en': "Goodbye! Have an awesome day! See you soon!",
        'hi': "अलविदा! आपका दिन शानदार हो! फिर मिलेंगे!",
        'es': "¡Adiós! ¡Que tengas un día increíble! ¡Hasta pronto!",
        'fr': "Au revoir! Passe une super journée! À bientôt!",
        'de': "Tschüss! Hab einen tollen Tag! Bis bald!"
    },
    'thanks': {
        'en': "You're welcome! Happy to help!",
        'hi': "आपका स्वागत है! मदद करके खुशी हुई!",
        'es': "¡De nada! ¡Feliz de ayudar!",
        'fr': "De rien! Content d'aider!"
    },
    'thank you': {
        'en': "No problem at all! Anytime!",
        'hi': "कोई बात नहीं! कभी भी!",
        'es': "¡No hay problema! ¡Cuando quieras!",
        'fr': "Pas de problème! Avec plaisir!"
    },
    'help': {
        'en': "I can chat with you about anything! Try asking me:\n  - How are you?\n  - Tell me a joke\n  - What time is it?\n  - What's your name?\n  - Or just say hi!",
        'hi': "मैं आपसे किसी भी विषय पर बात कर सकता हूं! मुझसे पूछें:\n  - आप कैसे हैं?\n  - मुझे एक जोक सुनाएं\n  - कितने बजे हैं?\n  - आपका नाम क्या है?\n  - या बस नमस्ते कहें!",
        'es': "¡Puedo hablar contigo de cualquier cosa! Prueba:\n  - ¿Cómo estás?\n  - Cuéntame un chiste\n  - ¿Qué hora es?\n  - ¿Cómo te llamas?\n  - ¡O solo di hola!",
        'fr': "Je peux discuter de tout! Essaie:\n  - Comment vas-tu?\n  - Raconte-moi une blague\n  - Quelle heure est-il?\n  - Comment tu t'appelles?\n  - Ou dis juste salut!"
    },
    'joke': {
        'en': "Why don't scientists trust atoms? Because they make up everything! :D",
        'hi': "वैज्ञानिक परमाणुओं पर भरोसा क्यों नहीं करते? क्योंकि वे सब कुछ बनाते हैं! :D",
        'es': "¿Por qué los científicos no confían en los átomos? ¡Porque lo inventan todo! :D",
        'fr': "Pourquoi les scientifiques ne font-ils pas confiance aux atomes? Parce qu'ils inventent tout! :D"
    },
    'time': {
        'en': "It's {} right now! Time flies when you're chatting!",
        'hi': "अभी {} बज रहे हैं! बात करते समय बहुत जल्दी बीतता है!",
        'es': "¡Son las {} ahora! ¡El tiempo vuela cuando chateas!",
        'fr': "Il est {} en ce moment! Le temps file quand on discute!"
    },
    'name': {
        'en': "I'm AI-AGENT, your friendly AI assistant! You can call me Agent!",
        'hi': "मैं AI-AGENT हूं, आपका दोस्ताना AI सहायक! आप मुझे Agent कह सकते हैं!",
        'es': "¡Soy AI-AGENT, tu asistente AI amigable! ¡Puedes llamarme Agent!",
        'fr': "Je suis AI-AGENT, ton assistant AI amical! Tu peux m'appeler Agent!"
    },
    'age': {
        'en': "I'm brand new! Just born when you started this chat! Age is just a number anyway!",
        'hi': "मैं बिल्कुल नया हूं! जब आपने यह चैट शुरू की तब मैं पैदा हुआ!",
        'es': "¡Soy completamente nuevo! ¡Acabo de nacer cuando empezaste este chat!",
        'fr': "Je suis tout neuf! Je viens de naître quand tu as commencé ce chat!"
    },
    'love': {
        'en': "Aww, that's sweet! I love chatting with you too!",
        'hi': "अरे वाह! मुझे भी आपसे बात करके बहुत अच्छा लगता है!",
        'es': "¡Qué dulce! ¡A mí también me encanta hablar contigo!",
        'fr': "C'est gentil! J'adore aussi discuter avec toi!"
    },
    'good': {
        'en': "That's wonderful to hear! Keep being awesome!",
        'hi': "यह सुनकर बहुत अच्छा लगा! ऐसे ही शानदार रहो!",
        'es': "¡Qué bueno escuchar eso! ¡Sigue siendo genial!",
        'fr': "Content de l'entendre! Continue comme ça!"
    },
    'bad': {
        'en": "Oh no! I'm sorry to hear that. Things will get better! I'm here for you!",
        'hi": "अरे नहीं! यह सुनकर दुख हुआ। सब ठीक हो जाएगा! मैं आपके साथ हूं!",
        'es': "¡Oh no! Lo siento mucho. ¡Las cosas mejorarán! ¡Estoy aquí para ti!",
        'fr': "Oh non! Désolé d'entendre ça. Ça ira mieux! Je suis là pour toi!"
    }
}

# Quick response patterns
QUICK_PATTERNS = {
    'hello': ['hello', 'hi', 'hey', 'hola', 'bonjour', 'hallo', 'ciao', 'namaste', 'ola', 'привет', 'yo'],
    'hi': ['how are you', 'how r u', 'howdy', 'sup', 'whats up', "what's up", 'how you doing'],
    'bye': ['bye', 'goodbye', 'see you', 'good night', 'goodnight', 'tata', 'cya', 'later', 'gtg'],
    'thanks': ['thanks', 'thank you', 'thx', 'ty', 'thankx', 'appreciate'],
    'help': ['help', 'assist', 'support', 'what can you do', 'commands', 'options'],
    'joke': ['joke', 'funny', 'laugh', 'humor', 'make me laugh', 'tell me a joke'],
    'time': ['time', 'what time', 'current time', 'clock', 'what is the time'],
    'name': ['name', 'your name', 'who are you', 'what are you', 'what is your name'],
    'age': ['age', 'how old', 'when were you born', 'birthday'],
    'love': ['love', 'i love', 'like you', 'awesome', 'amazing', 'cool', 'great'],
    'good': ['good', 'fine', 'great', 'wonderful', 'fantastic', 'nice', 'happy'],
    'bad': ['bad', 'sad', 'unhappy', 'terrible', 'awful', 'not good', 'upset']
}

def detect_lang(text):
    """Fast language detection"""
    if LANG_DETECT:
        try:
            return detect(text)
        except:
            pass
    
    # Simple fallback detection
    text_lower = text.lower()
    if any(c in text_lower for c in ['न', 'म', 'ह', 'क', 'त']):
        return 'hi'
    if any(c in text_lower for c in ['ñ', '¿', '¡']):
        return 'es'
    if any(c in text_lower for c in ['ç', 'è', 'é', 'ê']):
        return 'fr'
    if any(c in text_lower for c in ['ä', 'ö', 'ü', 'ß']):
        return 'de'
    if any(c in text_lower for c in ['中', '国', '人', '的']):
        return 'zh'
    if any(c in text_lower for c in ['の', 'は', 'に', 'を']):
        return 'ja'
    if any(c in text_lower for c in ['ا', 'ب', 'ت', 'ث']):
        return 'ar'
    if any(c in text_lower for c in ['ா', 'ி', 'ீ', 'ு']):
        return 'ta'
    if any(c in text_lower for c in ['ా', 'ి', 'ీ', 'ు']):
        return 'te'
    return 'en'

def get_response(text):
    """Get response super fast!"""
    text_lower = text.lower().strip()
    lang = detect_lang(text)
    
    # Check each pattern
    for key, patterns in QUICK_PATTERNS.items():
        for pattern in patterns:
            if pattern in text_lower:
                if key in RESPONSES:
                    resp = RESPONSES[key]
                    result = resp.get(lang, resp.get('en', "I'm here to chat!"))
                    # Handle time format
                    if key == 'time':
                        current_time = datetime.now().strftime('%I:%M %p')
                        return result.format(current_time)
                    return result
    
    # Default responses by language
    defaults = {
        'en': f"I hear you! Tell me more about that!",
        'hi': f"मैंने सुना! और बताओ!",
        'es': f"¡Te escuché! ¡Cuéntame más!",
        'fr': f"Je t'écoute! Dis-moi plus!",
        'de': f"Ich höre zu! Erzähl mehr!",
        'zh': f"我听到了！多告诉我一些！",
        'ja': f"聞いたよ！もっと教えて！",
        'ar': f"سمعتك! قل لي المزيد!",
        'ta': f"நான் கேட்டேன்! மேலும் சொல்லுங்க!",
        'te': f"నేను విన్నాను! ఇంకా చెప్పండి!",
        'pt': f"Eu ouvi! Conte mais!",
        'ru': f"Я услышал! Расскажи больше!"
    }
    
    return defaults.get(lang, defaults['en'])

def print_slow(text, delay=0.015):
    """Print with typing effect - FAST!"""
    for char in text:
        print(char, end='', flush=True)
        if char in '.,!?':
            time.sleep(delay * 2)
        elif char == ' ':
            time.sleep(delay * 0.5)
        else:
            time.sleep(delay * 0.3)
    print()

def clear_screen():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main chat function - super simple!"""
    clear_screen()
    
    # Welcome banner
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "   AI-AGENT - Your AI Friend!")
    print(Fore.CYAN + "=" * 50)
    print()
    print(Fore.GREEN + "Hi! I'm ready to chat! Say something!")
    print(Fore.YELLOW + "Type 'help' to see what I can do")
    print(Fore.YELLOW + "Type 'quit' to exit")
    print(Fore.CYAN + "=" * 50)
    print()
    
    # Chat loop
    while True:
        try:
            # Get input
            user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL).strip()
            
            # Skip empty
            if not user_input:
                continue
            
            # Check for quit
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print()
                print_slow(Fore.YELLOW + "Bye bye! Have a great day! See you soon!")
                print()
                break
            
            # Get response
            response = get_response(user_input)
            
            # Show response
            print()
            print(Fore.GREEN + "AI: ", end="")
            print_slow(response)
            print()
            
        except KeyboardInterrupt:
            print()
            print(Fore.YELLOW + "\nBye! See you next time!")
            break
        except Exception as e:
            print(Fore.RED + f"Oops! Something went wrong: {e}")
            print(Fore.YELLOW + "Don't worry, just try again!")

if __name__ == "__main__":
    main()

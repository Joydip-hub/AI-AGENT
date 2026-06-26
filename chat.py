"""
AI-AGENT - Your AI Friend!
Super simple, super fast!
"""

import os
import sys
import time
import json
from datetime import datetime

# Try to import colorama for colors
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    # Fake color class if colorama not installed
    class FakeFore:
        CYAN = ""
        GREEN = ""
        YELLOW = ""
        RED = ""
        BLUE = ""
        WHITE = ""
    class FakeStyle:
        RESET_ALL = ""
    Fore = FakeFore()
    Style = FakeStyle()

# Try to import langdetect
try:
    from langdetect import detect
    LANG_DETECT = True
except ImportError:
    LANG_DETECT = False

# ============================================
# SIMPLE RESPONSES - NO HEAVY AI NEEDED!
# ============================================

RESPONSES = {
    # Greetings
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
        'en': "I can chat with you about anything! Try asking me:\n- How are you?\n- Tell me a joke\n- What time is it?\n- Or just say hi!",
        'hi': "मैं आपसे किसी भी विषय पर बात कर सकता हूं! मुझसे पूछें:\n- आप कैसे हैं?\n- मुझे एक जोक सुनाएं\n- कितने बजे हैं?\n- या बस नमस्ते कहें!",
        'es': "¡Puedo hablar contigo de cualquier cosa! Prueba preguntarme:\n- ¿Cómo estás?\n- Cuéntame un chiste\n- ¿Qué hora es?\n- ¡O solo di hola!",
        'fr': "Je peux discuter de tout avec toi! Essaie de me demander:\n- Comment vas-tu?\n- Raconte-moi une blague\n- Quelle heure est-il?\n- Ou dis juste salut!"
    },
    'joke': {
        'en': "Why don't scientists trust atoms? Because they make up everything! 😄",
        'hi': "वैज्ञानिक परमाणुओं पर भरोसा क्यों नहीं करते? क्योंकि वे सब कुछ बनाते हैं! 😄",
        'es': "¿Por qué los científicos no confían en los átomos? ¡Porque lo inventan todo! 😄",
        'fr': "Pourquoi les scientifiques ne font-ils pas confiance aux atomes? Parce qu'ils inventent tout! 😄"
    },
    'time': {
        'en': f"It's {datetime.now().strftime('%I:%M %p')} right now! Time flies when you're chatting!",
        'hi': f"अभी {datetime.now().strftime('%I:%M %p')} बज रहे हैं! बात करते समय बहुत जल्दी बीतता है!",
        'es': f"¡Son las {datetime.now().strftime('%I:%M %p')} ahora! ¡El tiempo vuela cuando chateas!",
        'fr': f"Il est {datetime.now().strftime('%I:%M %p')} en ce moment! Le temps file quand on discute!"
    },
    'name': {
        'en': "I'm AI-AGENT, your friendly AI assistant! You can call me Agent!",
        'hi': "मैं AI-AGENT हूं, आपका दोस्ताना AI सहायक! आप मुझे Agent कह सकते हैं!",
        'es': "¡Soy AI-AGENT, tu asistente AI amigable! ¡Puedes llamarme Agent!",
        'fr': "Je suis AI-AGENT, ton assistant AI amical! Tu peux m'appeler Agent!"
    },
    'age': {
        'en': "I'm brand new! Just born when you started this chat! Age is just a number anyway!",
        'hi': "मैं बिल्कुल नया हूं! जब आपने यह चैट शुरू की तब मैं पैदा हुआ! उम्र तो बस एक नंबर है!",
        'es': "¡Soy completamente nuevo! ¡Acabo de nacer cuando empezaste este chat! ¡La edad es solo un número!",
        'fr': "Je suis tout neuf! Je viens de naître quand tu as commencé ce chat! L'âge n'est qu'un chiffre!"
    }
}

# Quick response patterns
QUICK_PATTERNS = {
    'hello': ['hello', 'hi', 'hey', 'hola', 'bonjour', 'hallo', 'ciao', 'namaste', 'ola', 'привет'],
    'hi': ['how are you', 'how r u', 'howdy', 'sup', 'whats up', "what's up"],
    'bye': ['bye', 'goodbye', 'see you', 'good night', 'goodnight', 'tata', 'cya'],
    'thanks': ['thanks', 'thank you', 'thx', 'ty', 'thankx'],
    'help': ['help', 'assist', 'support', 'what can you do'],
    'joke': ['joke', 'funny', 'laugh', 'humor', 'make me laugh'],
    'time': ['time', 'what time', 'current time', 'clock'],
    'name': ['name', 'your name', 'who are you', 'what are you'],
    'age': ['age', 'how old', 'when were you born']
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
                    return resp.get(lang, resp.get('en', "I'm here to chat!"))
    
    # Default responses by language
    defaults = {
        'en': f"I hear you! You said: '{text}'. Tell me more! I'm listening!",
        'hi': f"मैंने सुना! आपने कहा: '{text}'. और बताओ! मैं सुन रहा हूं!",
        'es': f"¡Te escuché! Dijiste: '{text}'. ¡Cuéntame más! ¡Te escucho!",
        'fr': f"Je t'écoute! Tu as dit: '{text}'. Dis-moi plus! J'écoute!",
        'de': f"Ich höre zu! Du hast gesagt: '{text}'. Erzähl mehr! Ich höre zu!",
        'zh': f"我听到了！你说的是：'{text}'. 多告诉我一些！我在听！",
        'ja': f"聞いたよ！君が言った：'{text}'. もっと教えて！聞いているよ！",
        'ar': f"سمعتك! قلت: '{text}'. قل لي المزيد! أنا أستمع!",
        'ta': f"நான் கேட்டேன்! நீங்க சொன்னீங்க: '{text}'. மேலும் சொல்லுங்க! கேட்டுக்கிட்டு இருக்கேன்!",
        'te': f"నేను విన్నాను! మీరు చెప్పారు: '{text}'. ఇంకా చెప్పండి! నేను వింటున్నాను!",
        'pt': f"Eu ouvi! Você disse: '{text}'. Conte mais! Estou ouvindo!",
        'ru': f"Я услышал! Ты сказал: '{text}'. Расскажи больше! Я слушаю!"
    }
    
    return defaults.get(lang, defaults['en'])

def print_slow(text, delay=0.02):
    """Print with typing effect - but faster!"""
    for char in text:
        print(char, end='', flush=True)
        if char in '.,!?':
            time.sleep(delay * 3)
        elif char == ' ':
            time.sleep(delay)
        else:
            time.sleep(delay * 0.5)
    print()

def main():
    """Main chat function - super simple!"""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Welcome banner
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "   🤖 AI-AGENT - Your AI Friend!")
    print(Fore.CYAN + "   Type anything to chat!")
    print(Fore.CYAN + "   Type 'quit' to exit")
    print(Fore.CYAN + "=" * 50)
    print()
    print(Fore.GREEN + "Hi! I'm ready to chat! Say something! 😊")
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
                print_slow(Fore.YELLOW + "👋 Bye bye! Have a great day! See you soon!")
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
            print(Fore.YELLOW + "\n👋 Bye! See you next time!")
            break
        except Exception as e:
            print(Fore.RED + f"Oops! Something went wrong: {e}")
            print(Fore.YELLOW + "Don't worry, just try again!")

if __name__ == "__main__":
    main()

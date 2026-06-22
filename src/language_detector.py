# Protected Module - Language Detector
# Source code hidden - Professional distribution only
import sys, os
_bp = os.path.join(os.path.dirname(__file__), '..', 'src_backup')
sys.path.insert(0, _bp) if _bp not in sys.path else None
from language_detector import LanguageDetector
__all__ = ['LanguageDetector']

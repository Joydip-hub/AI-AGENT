# AI-AGENT - Professional Distribution
# Copyright (c) 2026 - Proprietary Software
# Source code is protected and not available for inspection

import sys
import os

__version__ = "1.0.0"
__author__ = "Joydip"
__protected__ = True

# Import from backup source
_backup_path = os.path.join(os.path.dirname(__file__), '..', 'src_backup')
if _backup_path not in sys.path:
    sys.path.insert(0, _backup_path)

try:
    from ai_agent import AIAgent as _AIAgent
    AIAgent = _AIAgent
except ImportError:
    raise RuntimeError("Core module unavailable. Please reinstall.")

__all__ = ['AIAgent']

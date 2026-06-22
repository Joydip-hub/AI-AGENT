"""
Conversation Management System
Handles conversation flow, context, and state management
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

class ConversationManager:
    """
    Manages conversation state, context, and history
    """
    
    def __init__(self, storage_path: str = "./data/conversations"):
        """
        Initialize conversation manager
        
        Args:
            storage_path: Path to store conversation data
        """
        self.logger = logging.getLogger(__name__)
        self.storage_path = storage_path
        self.sessions = {}
        
        # Create storage directory if it doesn't exist
        os.makedirs(storage_path, exist_ok=True)
        
        self.logger.info(f"Conversation manager initialized with storage: {storage_path}")
    
    def create_session(self, session_id: str, user_info: Optional[Dict] = None) -> Dict:
        """
        Create a new conversation session
        
        Args:
            session_id: Unique session identifier
            user_info: Optional user information
            
        Returns:
            Session data dictionary
        """
        session = {
            'session_id': session_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'user_info': user_info or {},
            'messages': [],
            'metadata': {
                'language': 'en',
                'topic': None,
                'sentiment': 'neutral'
            }
        }
        
        self.sessions[session_id] = session
        self.logger.info(f"Created session: {session_id}")
        
        return session
    
    def get_session(self, session_id: str) -> Optional[Dict]:
        """
        Get existing session
        
        Args:
            session_id: Session identifier
            
        Returns:
            Session data or None if not found
        """
        return self.sessions.get(session_id)
    
    def add_message(self, session_id: str, role: str, content: str, 
                   language: Optional[str] = None, metadata: Optional[Dict] = None):
        """
        Add message to session
        
        Args:
            session_id: Session identifier
            role: 'user' or 'assistant'
            content: Message content
            language: Message language
            metadata: Additional metadata
        """
        session = self.get_session(session_id)
        if not session:
            self.logger.warning(f"Session not found: {session_id}")
            return
        
        message = {
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'language': language or session['metadata']['language'],
            'metadata': metadata or {}
        }
        
        session['messages'].append(message)
        session['updated_at'] = datetime.now().isoformat()
        
        self.logger.debug(f"Added {role} message to session {session_id}")
    
    def get_context(self, session_id: str, limit: int = 10) -> List[Dict]:
        """
        Get recent conversation context
        
        Args:
            session_id: Session identifier
            limit: Number of recent messages
            
        Returns:
            List of recent messages
        """
        session = self.get_session(session_id)
        if not session:
            return []
        
        return session['messages'][-limit:]
    
    def save_session(self, session_id: str) -> bool:
        """
        Save session to disk
        
        Args:
            session_id: Session identifier
            
        Returns:
            True if successful
        """
        session = self.get_session(session_id)
        if not session:
            return False
        
        try:
            filepath = os.path.join(self.storage_path, f"{session_id}.json")
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(session, f, ensure_ascii=False, indent=2)
            self.logger.info(f"Session saved: {session_id}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save session {session_id}: {e}")
            return False
    
    def load_session(self, session_id: str) -> Optional[Dict]:
        """
        Load session from disk
        
        Args:
            session_id: Session identifier
            
        Returns:
            Session data or None
        """
        try:
            filepath = os.path.join(self.storage_path, f"{session_id}.json")
            if not os.path.exists(filepath):
                return None
            
            with open(filepath, 'r', encoding='utf-8') as f:
                session = json.load(f)
            
            self.sessions[session_id] = session
            self.logger.info(f"Session loaded: {session_id}")
            return session
        except Exception as e:
            self.logger.error(f"Failed to load session {session_id}: {e}")
            return None
    
    def delete_session(self, session_id: str) -> bool:
        """
        Delete session
        
        Args:
            session_id: Session identifier
            
        Returns:
            True if successful
        """
        try:
            # Remove from memory
            if session_id in self.sessions:
                del self.sessions[session_id]
            
            # Remove from disk
            filepath = os.path.join(self.storage_path, f"{session_id}.json")
            if os.path.exists(filepath):
                os.remove(filepath)
            
            self.logger.info(f"Session deleted: {session_id}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to delete session {session_id}: {e}")
            return False
    
    def get_all_sessions(self) -> List[str]:
        """
        Get all session IDs
        
        Returns:
            List of session IDs
        """
        return list(self.sessions.keys())
    
    def get_session_stats(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Get session statistics
        
        Args:
            session_id: Session identifier
            
        Returns:
            Statistics dictionary
        """
        session = self.get_session(session_id)
        if not session:
            return None
        
        messages = session['messages']
        user_messages = [m for m in messages if m['role'] == 'user']
        assistant_messages = [m for m in messages if m['role'] == 'assistant']
        
        languages = set(m.get('language', 'unknown') for m in messages)
        
        return {
            'session_id': session_id,
            'total_messages': len(messages),
            'user_messages': len(user_messages),
            'assistant_messages': len(assistant_messages),
            'languages_used': list(languages),
            'created_at': session['created_at'],
            'updated_at': session['updated_at'],
            'duration_minutes': self._calculate_duration(session)
        }
    
    def _calculate_duration(self, session: Dict) -> float:
        """Calculate session duration in minutes"""
        try:
            created = datetime.fromisoformat(session['created_at'])
            updated = datetime.fromisoformat(session['updated_at'])
            duration = (updated - created).total_seconds() / 60
            return round(duration, 2)
        except Exception:
            return 0.0

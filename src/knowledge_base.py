"""
Knowledge Base Integration Module
Provides topic-based knowledge and information retrieval
"""

import logging
from typing import Dict, List, Optional, Any
import json

class KnowledgeBase:
    """
    Knowledge base for AI agent to access information on various topics
    """
    
    def __init__(self):
        """Initialize knowledge base"""
        self.logger = logging.getLogger(__name__)
        self.knowledge_store = self._initialize_knowledge()
        self.logger.info("Knowledge base initialized")
    
    def _initialize_knowledge(self) -> Dict[str, Any]:
        """
        Initialize knowledge store with various topics
        
        Returns:
            Knowledge dictionary
        """
        return {
            'general': {
                'greeting': 'I am an AI assistant designed to help with various topics.',
                'capabilities': [
                    'Answer questions on multiple topics',
                    'Provide information in multiple languages',
                    'Maintain conversation context',
                    'Assist with various tasks'
                ]
            },
            'science': {
                'physics': 'Physics is the natural science that studies matter, energy, and their interactions.',
                'chemistry': 'Chemistry studies the composition, structure, and properties of matter.',
                'biology': 'Biology is the study of living organisms and their interactions.',
                'astronomy': 'Astronomy studies celestial objects and phenomena in the universe.'
            },
            'technology': {
                'ai': 'Artificial Intelligence enables machines to perform tasks that typically require human intelligence.',
                'programming': 'Programming is the process of creating instructions for computers to execute.',
                'web_development': 'Web development involves building and maintaining websites and web applications.',
                'cybersecurity': 'Cybersecurity protects systems, networks, and data from digital attacks.'
            },
            'languages': {
                'programming_languages': ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust', 'Ruby', 'PHP'],
                'natural_languages': ['English', 'Spanish', 'French', 'German', 'Chinese', 'Hindi', 'Arabic', 'Japanese']
            },
            'mathematics': {
                'algebra': 'Algebra uses symbols and rules to manipulate mathematical expressions.',
                'calculus': 'Calculus studies continuous change through derivatives and integrals.',
                'geometry': 'Geometry deals with shapes, sizes, and properties of space.',
                'statistics': 'Statistics analyzes and interprets numerical data.'
            },
            'history': {
                'ancient': 'Ancient history covers human civilization from prehistory to the Middle Ages.',
                'modern': 'Modern history focuses on events from the 15th century to present.',
                'world_wars': 'The World Wars were global conflicts in the 20th century.'
            },
            'geography': {
                'continents': ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia', 'Antarctica'],
                'oceans': ['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern']
            },
            'arts': {
                'music': 'Music is an art form using sound organized in time.',
                'painting': 'Painting is the practice of applying pigment to a surface.',
                'literature': 'Literature includes written works of artistic value.',
                'cinema': 'Cinema is the art of creating motion pictures.'
            }
        }
    
    def search_knowledge(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Search knowledge base for relevant information
        
        Args:
            query: Search query
            
        Returns:
            Relevant knowledge or None
        """
        query_lower = query.lower()
        results = {}
        
        # Search through all categories
        for category, content in self.knowledge_store.items():
            if isinstance(content, dict):
                for key, value in content.items():
                    if query_lower in key.lower() or (isinstance(value, str) and query_lower in value.lower()):
                        if category not in results:
                            results[category] = {}
                        results[category][key] = value
            elif isinstance(content, list):
                if any(query_lower in str(item).lower() for item in content):
                    results[category] = content
        
        return results if results else None
    
    def get_category(self, category: str) -> Optional[Dict[str, Any]]:
        """
        Get all knowledge from a specific category
        
        Args:
            category: Category name
            
        Returns:
            Category knowledge or None
        """
        return self.knowledge_store.get(category)
    
    def get_all_categories(self) -> List[str]:
        """
        Get all available categories
        
        Returns:
            List of category names
        """
        return list(self.knowledge_store.keys())
    
    def add_knowledge(self, category: str, key: str, value: Any) -> bool:
        """
        Add new knowledge to the store
        
        Args:
            category: Category name
            key: Knowledge key
            value: Knowledge value
            
        Returns:
            True if successful
        """
        try:
            if category not in self.knowledge_store:
                self.knowledge_store[category] = {}
            
            if isinstance(self.knowledge_store[category], dict):
                self.knowledge_store[category][key] = value
            else:
                self.logger.warning(f"Category {category} is not a dictionary")
                return False
            
            self.logger.info(f"Added knowledge: {category}.{key}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to add knowledge: {e}")
            return False
    
    def get_topic_info(self, topic: str) -> Optional[str]:
        """
        Get information about a specific topic
        
        Args:
            topic: Topic name
            
        Returns:
            Information string or None
        """
        # Search across all categories for the topic
        for category, content in self.knowledge_store.items():
            if isinstance(content, dict) and topic.lower() in content:
                return content[topic.lower()]
        
        return None

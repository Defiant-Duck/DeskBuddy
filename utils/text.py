# utils/text.py
"""Text utility functions for the DeskBuddy application."""
import string

def normalize_text(text: str) -> str:
    """
    Normalize text by converting to lowercase, stripping whitespace, and removing punctuation.

    Args:
        text: The input text to normalize

    Returns:
        The normalized text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Replace specific punctuation with spaces
    for char in ['-', ',', '.']:
        text = text.replace(char, ' ')
    
    # Remove remaining punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    # Strip whitespace and normalize spaces
    text = ' '.join(text.split())
    
    return text
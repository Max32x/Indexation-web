import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Charger les stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords


# Liste des stopwords
STOPWORDS = stopwords.words('english')

def tokenize_nltk(text):
    """Tokenise un texte en utilisant NLTK."""
    tokens = word_tokenize(text)
    return tokens

def normalize(tokens):
    """Normalise les tokens en les mettant en minuscule."""
    return [token.lower() for token in tokens]

def remove_stopwords(tokens):
    """Enlève les stopwords des tokens."""
    return [token for token in tokens if token not in STOPWORDS]

def tokenize(text):
    """Tokenise, normalise et filtre les stopwords d'un texte.
    
    Args:
        text (str): Le texte à traiter
        
    Returns:
        list: Liste des tokens traités
    """
    tokens = tokenize_nltk(text)
    normalized_tokens = normalize(tokens)
    result = remove_stopwords(normalized_tokens)
    return result

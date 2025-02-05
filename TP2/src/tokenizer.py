import os

def load_stopwords(file_path="data/STOPWORDS.txt"):
    """Charge les stopwords depuis le fichier texte."""
    stopwords = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Ignore les commentaires et les lignes vides
                line = line.strip()
                if line and not line.startswith('#'):
                    stopwords.add(line.lower())
    except FileNotFoundError:
        print(f"Attention: Fichier de stopwords non trouvé: {file_path}")
        return set()
    return stopwords

# Chargement des stopwords
STOPWORDS = load_stopwords(os.path.join(os.path.dirname(__file__), "../data/STOPWORDS.txt"))

def clean_and_tokenize(text):
    """Nettoie et tokenize le texte en filtrant les stopwords."""
    
    # Supprimer la ponctuation
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    # Tokenization par espace
    tokens = cleaned_text.split()
    
    # Filtrage des stopwords
    filtered_tokens = [token for token in tokens if token not in STOPWORDS]
    
    return filtered_tokens
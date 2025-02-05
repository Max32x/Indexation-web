from .tokenizer import tokenize

def assert_one_token(query_tokens, index_key):
    """Vérifie si au moins un token de la requête est présent dans l'index.
    
    Args:
        query_tokens (list) : Une liste de tokens
        index_key (str): Une clé de l'index à comparer avec les tokens de la requête.
        
    Returns:
        bool: True si au moins un token est trouvé, False sinon
    """
    index_tokens = tokenize(index_key)

    for token in query_tokens:
        if token in index_tokens:
            return True
    return False


def assert_all_tokens_in_index(query_tokens, index_key):
    """
    Vérifie si tous les tokens de la requête sont présents dans une clé de l'index.
    
    Args:
        query_tokens (list): liste de token lié à la query
        index_key (str): Une clé de l'index à comparer avec les tokens de la requête.
    
    Returns:
        bool: 
            - True si tous les tokens de la requête sont présents dans la clé de l'index.  
            - False sinon.
    """

    index_tokens = tokenize(index_key)
    
    for token in query_tokens:
        if token not in index_tokens:
            return False
    return True

def filter_index(query_tokens, index):
    """
    Filtre un index en fonction d'une requête, en retournant les clés de l'index 
    où au moins un token de la requête est trouvé.
    
    Args:
        query_tokens (list): 
        index (dict): L'index à filtrer (clé: chaîne, valeur: données associées).
    
    Returns:
        dict: Un nouvel index filtré.
    """
    filtered_index = {}

    for index_key, value in index.items():
        # Appliquer les critères de filtrage
        if assert_one_token(query_tokens, index_key):
            filtered_index[index_key] = value
    
    return filtered_index

from .tokenizer import clean_and_tokenize

def build_position_index(documents, key):
    """Construit un index inversé avec les positions des mots pour un champ donné.
    
    Args:
        documents: Liste des documents à indexer
        key: Champ sur lequel construire l'index (ex: "title", "description")
    
    Returns:
        Dict: Index inversé avec positions {mot: [{url, position}, ...]}
    """
    position_index = {}

    for doc in documents:
        text = doc.get(key, "")
        url = doc.get("url")

        # Tokenization et nettoyage
        tokens = clean_and_tokenize(text)

        # Construction de l'index avec positions
        for position, token in enumerate(tokens):
            if token not in position_index:
                position_index[token] = []
            position_index[token].append({"url": url, "position": position})
    
    return position_index


def build_reviews_index(documents):
    """Construit un index des avis pour chaque produit.
    
    Args:
        documents: Liste des documents contenant les avis
    
    Returns:
        Dict: Index des métriques d'avis par URL
    """
    reviews_index = {}

    for doc in documents:
        url = doc.get("url")
        reviews = doc.get("product_reviews", [])
        
        # Initialisation des métriques
        total_reviews = len(reviews)
        average_rating = sum(review.get("rating", 0) for review in reviews) / total_reviews if total_reviews > 0 else 0
        last_rating = reviews[-1].get("rating") if total_reviews > 0 else None
        
        # Store in the index
        reviews_index[url] = {
            "total_reviews": total_reviews,
            "average_rating": round(average_rating, 2),
            "last_rating": last_rating
        }

    return reviews_index




def build_features_index(documents, feature):
    """Construit un index inversé pour une caractéristique de produit donnée.
    
    Args:
        documents: Liste des documents à indexer
        feature: Caractéristique à indexer (ex: "brand", "material")
    
    Returns:
        Dict: Index inversé {valeur_caracteristique: [urls]}
    """
    feature_index = {}

    for doc in documents:
        url = doc.get("url")
        features = doc.get("product_features", {})
        
        feature_value = features.get(feature)

        # cleaned_feature_value = clean_and_tokenize(feature_value)

        # Indexing brand
        if feature_value:
            if feature_value not in feature_index:
                feature_index[feature_value] = []
            feature_index[feature_value].append(url)

    return feature_index


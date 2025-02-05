import json 
import os

def load_json_index(feature):
    """Charge un index inversé depuis un fichier JSON.
    
    Args:
        feature: Le nom de l'index à charger (ex: 'title', 'description', 'reviews')
        
    Returns:
        list: Les données de l'index chargé ou une liste vide en cas d'erreur
    """
    data = []
    try:
        # Construire le chemin correct du fichier en remontant à la racine du projet
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", f"{feature}_index.json")
        # print(file_path)

        with open(file_path, 'r', encoding='utf-8') as reader:
            data = json.load(reader)
        
        # print(f"Nombre de documents chargés : {len(data)}")
        return data
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        return []  # Return empty list instead of None


def load_synonyms():
    """Charge le dictionnaire des synonymes depuis un fichier JSON.
    
    Returns:
        dict: Le dictionnaire des synonymes ou une liste vide en cas d'erreur
    """
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", "origin_synonyms.json")
        with open(file_path, 'r', encoding='utf-8') as f:
            synonyms = json.load(f)
        return synonyms
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        return []  # Return empty list instead of None



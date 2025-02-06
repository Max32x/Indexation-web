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


def get_doc_feature(url, feature):
    # Ouvrir le fichier JSONL et lire les lignes

    if feature == "reviews" :
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", "reviews_index.json")
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.loads(file)

            # Check if the URL matches and return the mean mark
            if url in data:
                return data[url]['mean_mark']
            else:
                return None  # URL not found in the data


    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "data", "rearranged_products.jsonl")
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Charger chaque ligne en tant que dictionnaire JSON
            data = json.loads(line)
            
            # Si l'URL correspond, renvoyer la valeur de la feature demandée
            if data['url'] == url:

                if feature in ["title","description"]:
                    return data.get(feature)

                else :
                    return data.get("product_features").get(feature)
                
                return None
    
    # Si l'URL n'est pas trouvée dans le fichier
    return "URL non trouvée"

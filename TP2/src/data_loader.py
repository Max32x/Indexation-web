import json 
import os

def load_json(file_name):
    """Charge et lit un fichier JSONL et affiche des informations sur son contenu."""
    data = []
    try:
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", file_name)
        with open(file_path, 'r', encoding='utf-8') as reader:
            for line in reader:
                data.append(json.loads(line))
        
        print(f"Nombre de documents chargés : {len(data)}")
        return data
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        return []  # Return empty list instead of None

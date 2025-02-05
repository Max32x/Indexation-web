import json 

def load_json(file_path):
    """Charge et lit un fichier JSONL et affiche des informations sur son contenu."""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as reader:
            for line in reader:
                data.append(json.loads(line))
        
        print(f"Nombre de documents chargés : {len(data)}")
        return data
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur lors du chargement du fichier : {e}")

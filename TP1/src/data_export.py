import json
import os

def save_results_to_json(data_to_export ,filename="results_TP1.json"):
    """Sauvegarde les résultats du crawl dans un fichier JSON."""
    try:
        absolute_path = os.path.join(os.getcwd(), "TP1", "data", filename)
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(absolute_path, json_file, ensure_ascii=False, indent=4)
        

        print(f"Résultats sauvegardés dans {absolute_path}")
        
    except (IOError, OSError) as e:
        print(f"Erreur lors de la sauvegarde des résultats: {e}")

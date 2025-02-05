import json 
import os

def export_data(file_to_export, file_name):
    """Sauvegarde les résultats dans un fichier JSON."""
    try:
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(file_to_export, json_file, ensure_ascii=False, indent=4)
        # Affiche le chemin absolu vers le fichier sauvegardé
        absolute_path = os.path.abspath(file_name)
        print(f"Résultats sauvegardés dans {absolute_path}")
        
    except (IOError, OSError) as e:
        print(f"Erreur lors de la sauvegarde des résultats: {e}")

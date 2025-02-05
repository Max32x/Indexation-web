# Exemple d'utilisation
import os
from src.data_loader import load_json
from src.indexer import build_position_index, build_reviews_index, build_features_index
from src.data_export import export_data

if __name__ == "__main__":
    
    # Définition du chemin d'export pour les index inversés
    EXPORT_PATH = os.path.join(os.path.dirname(__file__), "data", "inverted_indexes")

    # Chargement des données depuis le fichier JSONL
    data = load_json(file_path=os.path.join(os.path.dirname(__file__), "./data/products.jsonl"))

    # Construction et export de l'index des titres
    title_index = build_position_index(data, "title")
    export_data(title_index, os.path.join(EXPORT_PATH, "title_index.json"))

    # Construction et export de l'index des descriptions
    description_index = build_position_index(data, "description")
    export_data(description_index, os.path.join(EXPORT_PATH, "description_index.json"))

    # Construction et export de l'index des avis
    reviews_index = build_reviews_index(data)
    export_data(reviews_index, os.path.join(EXPORT_PATH, "reviews_index.json"))

    # Construction et export des index pour chaque caractéristique de produit
    for feature in list(data[1]["product_features"].keys()):
        print('---', feature)
        feature_index = build_features_index(data, feature)
        export_data(feature_index, os.path.join(EXPORT_PATH, "features_index", f"{feature}_index.json"))

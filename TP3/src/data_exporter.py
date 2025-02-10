import json
import os
from src.data_loader import get_doc_feature

def export_query_results_to_json(query: str, ranking_results: list):
    """
    Exporte les résultats d'une requête en fichier JSON formaté.

    :param query: La requête de recherche.
    :param ranking_results: Liste de documents rangée par ordre décroissant de score.
    """

    # Préparer les données formatées
    formatted_results = {
        "query": query,
        "total_documents": len(ranking_results),
        "filtered_documents": [
            {
                "title": get_doc_feature(doc[0], "title"),
                "url": doc[0],
                "description": get_doc_feature(doc[0], "description"),
                "ranking_score": doc[1],
            }
            for doc in ranking_results
        ]
    }
    print(json.dumps(formatted_results, indent=4))

    # Définir le chemin du fichier
    file_name = f"{query}-search_results.json"
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base_path, "results")
    file_path = os.path.join(results_dir, file_name)

    # Vérification et création du répertoire si nécessaire
    os.makedirs(results_dir, exist_ok=True)

    # Exporter les résultats en JSON
    try:
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(formatted_results, json_file, indent=4, ensure_ascii=False)
        print(f"Les résultats ont été exportés avec succès dans '{file_path}'")

    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        return []  # Return empty list instead of None

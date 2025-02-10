from src.searcher import search_feature
from src.tokenizer import tokenize
from src.filtering import assert_all_tokens_in_index
from src.data_loader import get_doc_feature
from src.data_exporter import export_query_results_to_json
import math

def compute_bm25(query_tokens, doc_feature, feature, index, k1=1.5, b=0.75):
    """
    Compute BM25 score for a document with respect to a query.

    Args:
        query (list): A list of query tokens.
        document (str): A document to rank.
        index (dict): The inverted index.
        k1 (float): The term frequency scaling factor.
        b (float): The length normalization factor.

    Returns:
        float: The BM25 score for the document.
    """

    # Calculate the length of the document and the average document length
    doc_length = len(doc_feature.split())


    unique_urls = set()
    for category in index.values():
        # print(category)
        if feature in ["title", "description"]:
            unique_urls.update(category.keys())
        else :
            unique_urls.update(category)

    # Retourner le nombre d'URLs uniques
    total_url_count = len(unique_urls)

    # Calculate the total length of all documents
    total_length = sum(len(get_doc_feature(url, feature).split()) for url in unique_urls)

    # Compute the average document length
    avg_doc_length = total_length / total_url_count

    # print('---')
    # print(doc_feature)
    # print(doc_length)
    # print(avg_doc_length)
    # print(total_url_count)
    
    score = 0
    for term in query_tokens:
        # print(term)
        # If the term exists in the document
        if term in index:
            doc_freq = len(index[term])  # le nombre de documents contenant term
            idf = math.log((total_url_count - doc_freq + 0.5) / (doc_freq + 0.5) + 1.0)
            
            tf = doc_feature.lower().split().count(term)  # term frequency in the document
            score += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * doc_length / avg_doc_length))

            # print(idf, tf, score)

    return score


def rank_documents_feature(query, feature):
    """
    Classe les documents de l'index en fonction de leur pertinence par rapport à une requête.

    Args:
        query (str): La requête de l'utilisateur.
        feature

    Returns:
        list: Une liste de documents classés par pertinence (score BM25).
    """

    filtered_index = search_feature(query, feature)
    query_tokens = tokenize(query)

    # print(filtered_index)

    scores = {}

    for _, list_urls in filtered_index.items():
        
        # print(list_urls)

        # if feature = title or description, list_urls is a dict, it's a list otherwise
        for doc_url in (list_urls.keys() if feature in ["title", "description"] else list_urls): 
            doc_feature = get_doc_feature(doc_url, feature)
            score = compute_bm25(query_tokens, doc_feature, feature, filtered_index)

            if feature in ["title", "description"]:
                position = list_urls[doc_url][0]
                # print(doc_url, position)
                score += 1 / (position +1) #+1 POUR EVITER LA DIVISION PAR 0

            # print(query_tokens,'||||', doc_feature)

            if assert_all_tokens_in_index(query_tokens, doc_feature):
                score += 10  # Bonus pour les matchs exacts

            # print(score)

            scores[doc_url] = score

    return scores




def rank_documents(query):
    """
    Classe les documents de l'index en fonction de leur pertinence par rapport à une requête en utilisant différentes features pondérées.

    Args:
        query (str): La requête de l'utilisateur.

    Returns:
        list: Une liste de documents classés par pertinence.
    """
    FEATURES = ["title", "description", "brand", "domain"]

    COEFFICIENTS = {
        "title": 10,
        "description": 5,
        "brand": 8,
        "domain": 20
        # "origin": 2,
        # "reviews": 1
    }

    total_scores = {}

    for feature in FEATURES:

        # print('======================')
        # print(feature)
    

        # Calculer les scores pour chaque feature
        feature_scores = rank_documents_feature(query, feature)
        # print(sorted(feature_scores.items(), key=lambda x: x[1], reverse=True))

        # Ajouter les scores pondérés pour chaque URL
        for doc_url, score in feature_scores.items():
            if doc_url not in total_scores:
                
                mean_mark = get_doc_feature(doc_url, "review")
                if mean_mark:
                    total_scores[doc_url] = mean_mark/5 #Léger bonus pour les articles avec un avis
                total_scores[doc_url] = 0

            total_scores[doc_url] += score * COEFFICIENTS[feature]

    # Trier les documents par score décroissant
    ranked_docs = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)

    export_query_results_to_json(query, ranked_docs)

    return ranked_docs

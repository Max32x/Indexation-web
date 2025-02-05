from src.searcher import search
from src.tokenizer import tokenize
from src.filtering import assert_all_tokens_in_index
from src.data_loader import get_doc_feature
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
        # Ajouter chaque URL dans le set (les doublons seront automatiquement supprimés)
        unique_urls.update(category.keys())
    # Retourner le nombre d'URLs uniques
    total_url_count = len(unique_urls)

    avg_doc_length = sum(len(get_doc_feature(url,feature).split()) for url in index.keys()) / total_url_count

    print('---')
    print(doc_feature)
    print(doc_length)
    print(avg_doc_length) #problème
    print(total_url_count)
    
    score = 0
    for term in query_tokens:
        print(term)
        # If the term exists in the document
        if term in index:
            doc_freq = len(index[term])  # le nombre de documents contenant term
            idf = math.log((total_url_count - doc_freq + 0.5) / (doc_freq + 0.5) + 1.0)
            
            tf = doc_feature.lower().split().count(term)  # term frequency in the document
            score += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * doc_length / avg_doc_length))

            print(idf, tf, score)

    return score


def rank_documents(query, feature):
    """
    Classe les documents de l'index en fonction de leur pertinence par rapport à une requête.

    Args:
        query (str): La requête de l'utilisateur.
        feature

    Returns:
        list: Une liste de documents classés par pertinence (score BM25).
    """

    filtered_index = search(query, feature)
    query_tokens = tokenize(query)

    print(filtered_index)

    scores = {}

    for index_value, dict_value in filtered_index.items():
        # print('================')
        # print(index_value,'||||', dict_value)

        for doc_url in dict_value.keys():

            doc_feature = get_doc_feature(doc_url, feature)

            # Calculer le score BM25 pour chaque document
            score = compute_bm25(query_tokens, doc_feature, feature, filtered_index ) #probleme
            
            if assert_all_tokens_in_index(query_tokens, doc_feature):
                score += 10  # Bonus pour les matchs exacts

            # Ajouter le score dans le dictionnaire des scores
            scores[doc_url] = score

    # Trier les documents par score décroissant
    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    return ranked_docs







# def rank_documents(query, feature, index):

#     documents= search(query,feature)

#     avgdl = sum(len(doc['description'].split()) for doc in documents) / len(documents)

#     query_terms = tokenize(query)
#     ranked_results = []

#     for doc in documents:
#         score = compute_bm25(query_terms, doc['description'], index, avgdl)
#         if assert_all_tokens_in_index(query_terms, doc['description']):
#             score += 10  # Bonus pour les matchs exacts
#         ranked_results.append((doc, score))

#     # Trier par score décroissant
#     ranked_results.sort(key=lambda x: x[1], reverse=True)
#     return ranked_results

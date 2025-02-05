from src.data_loader import load_json_index, load_synonyms
from src.filtering import filter_index

def expand_query_with_synonyms(query):
    """
    Expands a query by adding its synonyms.

    Args:
        query (list): A list of tokens from the query.
        synonyms (dict): A dictionary where keys are tokens and values are lists of synonyms.

    Returns:
        list: An expanded list of query tokens, including synonyms.
    """
    expanded_query = set(query)
    
    for token in query:
        if token in synonyms:
            expanded_query.update(synonyms[token])
    
    return list(expanded_query)


def search(query):


    index= load_json_index("title")

    for query in 

    filtered_index= filter_index(query, index)
    return filtered_index



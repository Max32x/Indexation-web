from src.data_loader import load_json_index, load_synonyms
from src.filtering import filter_index
from src.tokenizer import tokenize

def expand_query_with_synonyms(query):
    """
    Expands a query by adding its synonyms.

    Args:
        query (list): A list of tokens from the query.
        synonyms (dict): A dictionary where keys are tokens and values are lists of synonyms.

    Returns:
        list: An expanded list of query tokens, including synonyms.

    Exemple:
        >>> expand_query_with_synonyms("USA Box" 
        ['united states', 'usa', 'box', 'united states of america', 'america']    
    """

    synonyms=load_synonyms()
    
    tokenized_query = tokenize(query)
    expanded_query = set(tokenized_query)

    for token in tokenized_query:
        if token in synonyms:
            expanded_query.update(synonyms[token])
    
    return list(expanded_query)


def search_feature(query, feature):

    index= load_json_index(feature)
    expanded_query=expand_query_with_synonyms(query)
    filtered_index= filter_index(expanded_query, index)

    return filtered_index



# Exemple d'utilisation
import os
from src.searcher import search


if __name__ == "__main__":


    query= "Blue"
    result_query = search(query)

    print(len(result_query))

    print(result_query)

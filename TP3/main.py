# Exemple d'utilisation
import os
from src.ranker import rank_documents


if __name__ == "__main__":


    query= "Blue"
    rank= rank_documents(query,"title")
    print(rank)
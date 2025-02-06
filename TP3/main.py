# Exemple d'utilisation
from src.ranker import rank_documents


if __name__ == "__main__":

    query = "shoes"
    rank = rank_documents(query)
    print('|||||||||||||||||||||||||||||||||')
    print(rank)
# Indexation-web (TP1)


## Description

Ce projet est un crawler web qui parcourt les pages à partir d'une URL de départ.



## Installation

```bash
git clone https://github.com/Max32x/Indexation-web
cd Indexation-web
pip install -r requirements.txt
python main.py
```

## Utilisation

Pour utiliser le crawler, exécutez le fichier `main.py` avec Python.

## Résultat

Le résultat est sauvegardé dans le fichier `results-TP1.json`.


# Indexation-web (TP2)

## Structure des indices

Le projet inclut trois types principaux d'indices, chacun ayant une structure spécifique :

### 1. **Position Index**  
Un index inversé qui associe chaque mot aux positions où il apparaît dans un document spécifique.

```python
{
    "mot": [
        {"url": "page_url", "position": 0},
        {"url": "page_url", "position": 3}
    ]   
}
```

### 2. **Review Index**  
```python
{
    "url": {
        "total_reviews": 10,
        "average_rating": 4.5,
        "last_rating": 5
    }
}
```
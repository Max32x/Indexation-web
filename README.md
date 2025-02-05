# Indexation-web (TP1)


## Description

Ce projet est un crawler web qui parcourt les pages à partir d'une URL de départ.



## Installation

```bash
git clone https://github.com/Max32x/Indexation-web
cd Indexation-web
pip install -r requirements.txt
python TP1/main.py
```

## Utilisation

Pour utiliser le crawler, exécutez le fichier `main.py` avec Python.

## Résultat

Le résultat est sauvegardé dans le fichier `results-TP1.json`.


# Indexation-web (TP2)


## Description

Ce projet crée des index inversé à partir d'un document semblable à celui généré par le TP1


## Installation

```bash
git clone https://github.com/Max32x/Indexation-web
cd Indexation-web
pip install -r requirements.txt
python TP2/main.py
```

## Résultat (Structure des indices)

Le projet inclut trois types principaux d'indices, chacun ayant une structure spécifique :

### 1. **Title/Description Index**  
Un index inversé qui associe chaque mot aux positions où il apparaît dans un document spécifique.

```python
"box": [
    {"url": "https://web-scraping.dev/product/1", "position": 0},
    {"url": "https://web-scraping.dev/product/13", "position": 3}
]   

```

### 2. **Review Index**  
Cet index stocke les informations sur les avis de produits. Il inclut le nombre d'avis, la note moyenne et la dernière note laissée.
```python
{
    "https://web-scraping.dev/product/1": {
        "total_reviews": 10,
        "average_rating": 4.5,
        "last_rating": 5
    }
}
```

### 3. **Feature Index**  
Un index inversé qui associe une caractéristique de produit (par exemple, la marque) à des URL de documents.

```python
{
    "ChocoDelight": [
        "https://web-scraping.dev/product/1",
        "https://web-scraping.dev/product/13"
    ],
    "GameFuel": [
        "https://web-scraping.dev/product/16",
        "https://web-scraping.dev/product/14",
        "https://web-scraping.dev/product/14?variant=one",
        "https://web-scraping.dev/product/14?variant=six-pack",

    ]
}
```
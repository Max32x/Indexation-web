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

Le résultat est sauvegardé dans le fichier `TP1/data/results-TP1.json`.

Exemple: 
```PYTHON
[
    {
        "title": "web-scraping.dev product page 1",
        "url": "https://web-scraping.dev/products/",
        "first_paragraph": "",
        "links": [
            "https://web-scraping.dev/",
            ...
            "https://web-scraping.dev/product/5",
            "https://web-scraping.dev/products?page=1",
            "https://web-scraping.dev/products?page=2",
            "https://web-scraping.dev/products?page=3"
        ]
    },
    {
        "title": "web-scraping.dev product Box of Chocolate Candy",
        "url": "https://web-scraping.dev/product/1",
        "first_paragraph": "Indulge your sweet tooth with our Box of Chocolate Candy. Each box contains an assortment of rich, flavorful chocolates with a smooth, creamy filling. Choose from a variety of flavors including zesty orange and sweet cherry. Whether you're looking for the perfect gift or just want to treat yourself, our Box of Chocolate Candy is sure to satisfy.",
        "links": [
            "https://web-scraping.dev/",
            "https://web-scraping.dev/product/1",
            ....
            "https://scrapfly.io/academy",
            "https://web-scraping.dev/"
        ]
    },
    ...
]
```
# Indexation-web (TP2)


## Description

Ce projet crée des index inversé à partir d'un document semblable à celui généré par le TP1


## Installation

```bash
git clone https://github.com/Max32x/Indexation-web
cd Indexation-web
pip install -r requirements.txt
```

```bash
python TP2/main.py
```

## Résultat (Structure des indices)

Le projet inclut trois types principaux d'indices, chacun ayant une structure spécifique :

### 1. **Title/Description Index**  
Un index inversé qui associe chaque mot aux positions où il apparaît dans un document spécifique.

```json
"box": [
    {"url": "https://web-scraping.dev/product/1", "position": 0},
    {"url": "https://web-scraping.dev/product/13", "position": 3}
]   

```

### 2. **Review Index**  
Cet index stocke les informations sur les avis de produits. Il inclut le nombre d'avis, la note moyenne et la dernière note laissée.
```json
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

```json
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
Ces fichiers sont sauvegardés dans le dossier `TP2/data/inverted_indexes`.

# Indexation-web (TP3)

## Description

Ce projet permet de classer les documents indexés en fonction de leur pertinence à l'aide de l'algorithme BM25. Les documents peuvent être filtrés et scorés en fonction de différentes caractéristiques telles que le titre, la description, la marque et le domaine.

## Installation

```bash
git clone https://github.com/Max32x/Indexation-web
cd Indexation-web
pip install -r requirements.txt
```

```bash
python TP3/main.py
```

## Utilisation

Pour classer les documents en fonction d'une requête, lancez simplement le fichier `main.py`. L'algorithme calcule les scores BM25 en fonction des différentes caractéristiques des documents, leur position dans les descriptions et leur pertinence globale.

### Fonctionnalités principales

- **Recherche par feature** : Les documents sont filtrés en fonction des features disponibles (titre, description, marque, domaine).
- **Scoring BM25** : L'algorithme BM25 est utilisé pour déterminer la pertinence des documents par rapport à une requête.
- **Export JSON** : Les résultats sont exportés dans un fichier JSON contenant les titres, URL, descriptions, scores et métadonnées.

## Exemple de structure de sortie JSON

```json
{
    "query": "shoes",
    "total_documents": 20,
    "filtered_documents": [
        {
            "title": "Running Shoes for Men",
            "url": "https://web-scraping.dev/product/21",
            "description": "Featuring a breathable upper and a cushioned midsole, these shoes provide excellent ventilation and shock absorption. With a sleek design and various color options, you can hit the road or the treadmill in style. Stay comfortable during your runs with our men's running shoes",
            "ranking_score": 156.53808264648626
        },
        {
            "title": "Running Shoes for Men - 12",
            "url": "https://web-scraping.dev/product/9?variant=12",
            "description": "Stay comfortable during your runs with our men's running shoes. The durable outsole offers solid traction, ensuring stability even on slippery surfaces. Featuring a breathable upper and a cushioned midsole, these shoes provide excellent ventilation and shock absorption",
            "ranking_score": 156.41124873935982
        },
        .....
  ]
}
```

Les résultats sont sauvegardés dans le dossier `TP3/results`. 

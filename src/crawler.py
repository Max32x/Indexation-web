import json
from queue import PriorityQueue
from src.fetch import fetch_url_content, can_fetch_url
from src.parser import parse_html_content

class WebCrawler:
    """Crawler web qui parcourt les pages à partir d'une URL de départ.
    
    Attributes:
        start_url (str): URL de départ pour le crawling
        max_pages (int): Nombre maximum de pages à crawler (défaut: 10)
    """

    def __init__(self, start_url, max_pages=10):
        self.start_url = start_url
        self.visited_urls = set()
        self.crawled_data = []  # Stocke les résultats à exporter
        self.url_queue = PriorityQueue()
        self.max_pages = max_pages
        self.pages_crawled = 0

    def add_url_to_queue(self, url):
        """Ajoute une URL à la file avec une priorité en fonction du token 'product'."""
        priority = 0 if "product" in url else 1
        self.url_queue.put((priority, url))

    def crawl(self):
        """Effectue le crawling"""
        self.add_url_to_queue(self.start_url)

        while not self.url_queue.empty() and self.pages_crawled < self.max_pages:
            _, current_url = self.url_queue.get()  

            # Ignorer les URLs déjà visitées
            if current_url in self.visited_urls:
                continue

            # Vérification si l'URL est accessible
            if not can_fetch_url(current_url):
                print(f"Accès interdit selon robots.txt: {current_url}")
                continue

            # Affichage de la page en cours
            print(f"Crawling ({self.pages_crawled + 1}): {current_url}")
            self.visited_urls.add(current_url)
            self.pages_crawled += 1

            # Récupération et parsing de la page
            content = fetch_url_content(current_url)
            result = parse_html_content(content, current_url)
            if not result:
                continue
            
            # Ajout du résultat au fichier JSON
            self.crawled_data.append(result)

            # Extraction des liens suivants
            for next_link in result["links"]:
                if next_link not in self.visited_urls:
                    self.add_url_to_queue(next_link) 


        print("\nCrawling terminé !")
        self.save_results_to_json()


    def save_results_to_json(self, filename="results.json"):
        """Sauvegarde les résultats du crawl dans un fichier JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(self.crawled_data, json_file, ensure_ascii=False, indent=4)
            print(f"Résultats sauvegardés dans {filename}")
        except (IOError, OSError) as e:
            print(f"Erreur lors de la sauvegarde des résultats: {e}")

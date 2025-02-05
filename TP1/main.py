"""Point d'entrée principal du crawler web.

Ce script initialise et exécute le crawler avec les paramètres de configuration définis.
"""

from src.crawler import WebCrawler


if __name__ == "__main__":
    
    START_URL = "https://web-scraping.dev/products/"
    MAX_PAGES = 2
    
    crawler = WebCrawler(START_URL, MAX_PAGES)
    crawler.crawl()
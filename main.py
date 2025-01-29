from src.crawler import WebCrawler

if __name__ == "__main__":
    start_url = "https://web-scraping.dev/products"
    crawler = WebCrawler(start_url, max_pages=50)
    crawler.crawl()

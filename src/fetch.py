from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import urllib.request
from urllib.robotparser import RobotFileParser


def can_fetch_url(url: str) -> bool:
    """Vérifie si le crawler est autorisé à accéder à l'URL selon robots.txt."""
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    robot_parser = RobotFileParser()
    robot_parser.set_url(robots_url)
    try:
        robot_parser.read()
    except Exception as e:
        print(f"Impossible de lire {robots_url}: {e}")
        return False

    return robot_parser.can_fetch("*", url)


def fetch_url_content(url: str) -> str:
    """Effectue une requête HTTP pour récupérer le contenu d'une page HTML."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Erreur lors de la récupération de {url}: {e}")
        return ""




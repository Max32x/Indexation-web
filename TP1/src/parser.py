from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_html_content(html_content: str, base_url: str) -> dict:
    """Parse le contenu HTML et extrait le titre, le premier paragraphe et les liens."""
    
    # Dictionnaire pour stocker les résultats
    result = {
        "title": None,
        "url": base_url,
        "first_paragraph": None,
        "links": []
    }
    
    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraction du titre
    title_tag = soup.title
    result["title"] = title_tag.string if title_tag else ""
    
    # Extraction du premier paragraphe
    first_paragraph_tag = soup.find('p')
    result["first_paragraph"] = first_paragraph_tag.text.strip() if first_paragraph_tag else ""
    
    # Extraction des liens
    for a_tag in soup.find_all('a', href=True):
        link_url = urljoin(base_url, a_tag['href'])
        result["links"].append(link_url)
    
    return result

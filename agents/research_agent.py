from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests

class ResearchAgent:
    def __init__(self):
        self.status = "idle"
        self.sources = []

    def run(self, query: str):
        self.sources = []
        self.status = "researching"
        # Simulate web/doc search
        results = []

        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=10)

        for result in results:
            url = result['href']
            try:
                html = requests.get(url, timeout=5).text
                soup = BeautifulSoup(html, 'html.parser')
                for tag in soup(['script', 'style']):
                    tag.decompose()
                text = ' '.join(soup.stripped_strings)
                self.sources.append({
                    "url": url,
                    "title": result["title"],
                    "text": text[:1000]
                })
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")

        self.status = "complete"
        return self.sources

import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "title": soup.title.string if soup.title else None,
        "headings": [h.get_text(strip=True) for h in soup.find_all("h2")],
        "links": [a["href"] for a in soup.find_all("a", href=True)]
    }

    return data

url = "https://example.com"
result = scrape_page(url)

print("Title:", result["title"])
print("Headings:", result["headings"])
print("Links:", result["links"])

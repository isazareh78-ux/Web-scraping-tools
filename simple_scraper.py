import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string if soup.title else "No title found"

print("Page Title:", title)

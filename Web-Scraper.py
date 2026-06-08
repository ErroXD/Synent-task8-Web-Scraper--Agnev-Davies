import requests
import time
import csv
import json
from bs4 import BeautifulSoup

BASE_URL = "https://www.books.toscrape.com/catalogue/"

START_URL = "https://www.books.toscrape.com/catalogue/page-1.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
}

def get_book_data(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")
    books = []
    for article in articles:
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text[2:]
        availability = article.find("p", class_="instock availability").text.strip()
        books.append({"title": title, "price": price, "availability": availability})
    return books

def next_page(soup):
    next_button = soup.find("li", class_="next")
    if next_button:
        return BASE_URL + next_button.a["href"]
    return None
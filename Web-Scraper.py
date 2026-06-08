import requests
from bs4 import BeautifulSoup
import csv
import json
import time

BASE_URL = "https://books.toscrape.com/catalogue/"

START_URL = "https://books.toscrape.com/catalogue/page-1.html"

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

def save_to_csv(books, filename="books.csv"):
    if not books:
        print("No books to save.")
        return

    fieldnames = list(books[0].keys())

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
        print(f"Saved {len(books)} books to {filename}")

def save_to_json(books, filename="books.json"):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)
        print(f"Saved {len(books)} books to {filename}")

def main():
    url = START_URL
    all_books = []
    max_pages = 5
    while url and len(all_books) < max_pages * 20:  # Assuming 20 books per page
        print(f"Scraping {url}...")
        books = get_book_data(url)
        all_books.extend(books)
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        url = next_page(soup)
        time.sleep(1)  # Be polite and avoid overwhelming the server

    save_to_csv(all_books)
    save_to_json(all_books)

    for book in all_books:
        print(f"Title: {book['title']}, Price: {book['price']}, Availability: {book['availability']}")
    print(f"Total books scraped: {len(all_books)}")

if __name__ == "__main__":
    main()

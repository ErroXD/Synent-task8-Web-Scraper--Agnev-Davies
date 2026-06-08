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

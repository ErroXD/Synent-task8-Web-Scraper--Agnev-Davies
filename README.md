# 📚 Web Scraper — Books to Scrape

A Python web scraper built with `requests` and `BeautifulSoup` that extracts book data (title, price, star rating, availability) from [books.toscrape.com](https://books.toscrape.com) and saves the results to both **CSV** and **JSON** formats.

---

## 🖥️ Demo Output

```
Starting web scraper...
Target site: https://books.toscrape.com/catalogue/page-1.html

Scraping page 1: https://books.toscrape.com/catalogue/page-1.html
  Found 20 books | Total so far: 20
Scraping page 2: https://books.toscrape.com/catalogue/page-2.html
  Found 20 books | Total so far: 40
Scraping page 3: https://books.toscrape.com/catalogue/page-3.html
  Found 20 books | Total so far: 60

Scraping complete! Total books collected: 60
Saved 60 books to 'books.csv'
Saved 60 books to 'books.json'

--- Sample Output (first 3 books) ---
  title          : A Light in the Attic
  price          : £51.77
  rating         : Three
  availability   : In stock

  title          : Tipping the Velvet
  price          : £53.74
  rating         : One
  availability   : In stock

  title          : Soumission
  price          : £50.10
  rating         : One
  availability   : In stock
```

---

## 📁 Project Structure

```
📦 Web-Scraper/
├── Web-Scraper.py      # Main scraper script
├── books.csv           # Output: extracted data in CSV format
├── books.json          # Output: extracted data in JSON format
└── README.md           # Project documentation
```

---

## ⚙️ Requirements

- Python 3.7 or higher
- pip (Python package manager)

### Dependencies

| Library        | Type        | Purpose                          |
|----------------|-------------|----------------------------------|
| `requests`     | Third-party | Sends HTTP requests to websites  |
| `beautifulsoup4` | Third-party | Parses and navigates HTML        |
| `csv`          | Built-in    | Writes data to CSV files         |
| `json`         | Built-in    | Writes data to JSON files        |
| `time`         | Built-in    | Adds polite delay between pages  |

---

## 🚀 Installation & Setup

**1. Clone or download the project**

```bash
git clone https://github.com/your-username/web-scraper.git
cd web-scraper
```

**2. Install the required libraries**

```bash
pip install requests beautifulsoup4
```

> If you have multiple Python versions, use:
> ```bash
> python -m pip install requests beautifulsoup4
> ```

**3. Run the scraper**

```bash
python Web-Scraper.py
```

---

## 🔧 Configuration

Open `Web-Scraper.py` and adjust these constants at the top of the file:

```python
# Controls how many pages to scrape (1 page = 20 books)
MAX_PAGES = 3          # Change to 50 to scrape all 1000 books

# Starting URL
START_URL = "https://books.toscrape.com/catalogue/page-1.html"

# Base URL used to build next-page links
BASE_URL = "https://books.toscrape.com/catalogue/"
```

| Setting     | Value       | Result              |
|-------------|-------------|---------------------|
| `MAX_PAGES = 1`  | 1 page  | 20 books            |
| `MAX_PAGES = 3`  | 3 pages | 60 books            |
| `MAX_PAGES = 10` | 10 pages| 200 books           |
| `MAX_PAGES = 50` | 50 pages| 1000 books (all)    |

---

## 📊 Output Format

### books.csv

```
title,price,rating,availability
A Light in the Attic,£51.77,Three,In stock
Tipping the Velvet,£53.74,One,In stock
Soumission,£50.10,One,In stock
```

### books.json

```json
[
    {
        "title": "A Light in the Attic",
        "price": "£51.77",
        "rating": "Three",
        "availability": "In stock"
    },
    {
        "title": "Tipping the Velvet",
        "price": "£53.74",
        "rating": "One",
        "availability": "In stock"
    }
]
```

---

## 🧠 How It Works

```
Website HTML
    │
    ▼
requests.get(url)        ← Fetches raw HTML from the server
    │
    ▼
BeautifulSoup(html)      ← Parses HTML into a navigable tree
    │
    ▼
find_all("article")      ← Locates every book container on the page
    │
    ▼
Extract fields           ← Title, price, rating, availability
    │
    ▼
get_next_page_url()      ← Finds the "next" button and follows it
    │
    ▼
csv.DictWriter           ← Saves all data to books.csv
json.dump()              ← Saves all data to books.json
```

### Key Techniques Used

- **HTTP Requests** — `requests.get()` fetches pages like a browser
- **HTML Parsing** — `BeautifulSoup` navigates the tag tree
- **Pagination** — `while` loop follows "next page" links automatically
- **Rate Limiting** — `time.sleep(1)` adds a 1-second delay between requests to be polite to the server
- **Data Export** — `csv.DictWriter` and `json.dump()` save structured data

---

## 🐛 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'requests'` | Library not installed | Run `python -m pip install requests beautifulsoup4` |
| `SSLCertVerificationError: Hostname mismatch` | URL has `www.` prefix | Use `https://books.toscrape.com` not `https://www.books.toscrape.com` |
| `ConnectionError` | No internet connection | Check your network connection |
| Script runs but no output files | Wrong working directory | `cd` into the folder where the script is saved before running |

---

## 📌 Notes

- This scraper targets [books.toscrape.com](https://books.toscrape.com) — a website **purpose-built for practising web scraping**. It is completely legal to scrape.
- Always check a website's `robots.txt` and Terms of Service before scraping any real website.
- The 1-second delay (`time.sleep(1)`) between requests is intentional — it prevents overloading the server.

---

## 👨‍💻 Author

**Agnev Davies**
Synent Tech — Task 8: Web Scraper

---

## 📄 License

This project is for educational purposes as part of the Synent Tech internship programme.

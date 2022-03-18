# News Scraper using RSS + Newspaper3k 

This project scrapes news articles from an RSS feed (e.g., BBC News) using **feedparser** and then downloads and parses the full articles with **newspaper3k**. It extracts useful metadata like title, author, publish date, and article content.

---

##  Features
- Parse RSS feeds using `feedparser`
- Download and parse full articles using `newspaper3k`
- Extract:
  - Title
  - Author(s)
  - Publish date
  - Full content text
- Handles missing metadata gracefully
- Limit the number of articles to avoid huge downloads
- Prints structured article information

---

##  Requirements
- Python 3.8+
- Libraries:
  - `newspaper3k` (article scraping and parsing)
  - `feedparser` (RSS feed parsing)

---

##  Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/news-scraper.git
cd News Scraping with Python
pip install -r requirements.txt
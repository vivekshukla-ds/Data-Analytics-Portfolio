# Quotes_Scraping

##  Project Overview
This project scrapes quotes and authors from [quotes.toscrape.com](http://quotes.toscrape.com) using **Python** and **BeautifulSoup**.  
After scraping, it randomly selects a quote and lets the user guess the author in an interactive game.  
Hints are provided after wrong guesses to make the game engaging.

---

##  Features
- Web scraping with `requests` + `BeautifulSoup`
- Pagination handling (scrapes all pages until "Next" button disappears)
- Stores quotes, authors, and bio links in a list of dictionaries
- Interactive guessing game with hints:
  - Birth date & place of author
  - First letter of author’s first name
  - First letter of author’s last name

---

## ️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/quotes-game.git
cd Quote Scraping
pip install -r requirements.txt
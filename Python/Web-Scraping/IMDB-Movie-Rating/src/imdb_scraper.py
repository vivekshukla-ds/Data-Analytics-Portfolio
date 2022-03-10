{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d91f2b8b-5b48-4e7e-9a72-103ae01c4a57",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3723cb0-597d-48c4-a830-c06b47b1ab56",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://www.imdb.com/chart/top/\"\n",
    "headers = {    \n",
    "    \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \"\n",
    "                  \"AppleWebKit/537.36 (KHTML, like Gecko) \"\n",
    "                  \"Chrome/120.0.0.0 Safari/537.36\", \"Accept-Language\": \"en-US,en;q=0.9\"\n",
    "}\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d933f14",
   "metadata": {},
   "outputs": [],
   "source": [
    "BASE_DIR = os.path.dirname(os.path.dirname(__file__))\n",
    "OUTPUT_DIR = os.path.join(BASE_DIR, \"outputs\")\n",
    "os.makedirs(OUTPUT_DIR, exist_ok=True)\n",
    "\n",
    "OUTPUT_FILE = os.path.join(OUTPUT_DIR, \"imdb_movies.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08fab8b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(url, headers=headers)\n",
    "if response.status_code != 200:\n",
    "    raise Exception(\"Failed to fetch IMDB page\")\n",
    "\n",
    "soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "# Each movie is inside <li class=\"ipc-metadata-list-summary-item\">\n",
    "movies = soup.select(\"li.ipc-metadata-list-summary-item\")\n",
    "print(f\"Movies found: {len(movies)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e2ddedfb-9717-4f06-b1e6-2f28d2dbe60d",
   "metadata": {},
   "outputs": [],
   "source": [
    "movie_data = []\n",
    "\n",
    "for movie in movies:\n",
    "    # Title\n",
    "    title_tag = movie.select_one(\"h3.ipc-title__text\")\n",
    "    title = title_tag.text.strip() if title_tag else \"N/A\"\n",
    "    \n",
    "    # Year\n",
    "    year_tag = movie.select_one(\"span.cli-title-metadata-item\")\n",
    "    year = year_tag.text.strip() if year_tag else \"N/A\"\n",
    "    \n",
    "    # Rating\n",
    "    rating_tag = movie.select_one(\"span.ipc-rating-star--rating\")\n",
    "    rating = rating_tag.text.strip() if rating_tag else \"N/A\"\n",
    "    \n",
    "    movie_data.append({\"Title\": title,\"Year\": year,\"Rating\": rating})\n",
    "    \n",
    "    time.sleep(0.1)  # small pause for safety"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9b4bb25d-2d1e-45e1-b9f0-c550c4ffe465",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Shawshank Redemption (1994) - Rating: 9.3\n",
      "The Godfather (1972) - Rating: 9.2\n",
      "The Dark Knight (2008) - Rating: 9.1\n",
      "The Godfather Part II (1974) - Rating: 9.0\n",
      "12 Angry Men (1957) - Rating: 9.0\n",
      "The Lord of the Rings: The Return of the King (2003) - Rating: 9.0\n",
      "Schindler's List (1993) - Rating: 9.0\n",
      "The Lord of the Rings: The Fellowship of the Ring (2001) - Rating: 8.9\n",
      "Pulp Fiction (1994) - Rating: 8.8\n",
      "The Good, the Bad and the Ugly (1966) - Rating: 8.8\n"
     ]
    }
   ],
   "source": [
    "# Print first 10 movies for testing\n",
    "for movie in movie_data[:10]:\n",
    "    print(f\"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a929998b-4a03-4c5c-95f0-0a7a09fc666c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IMDb data saved successfully to imdb_top_250_movies.csv!\n"
     ]
    }
   ],
   "source": [
    "#Save the data into a CSV file\n",
    "df = pd.DataFrame(movie_data)\n",
    "df.to_csv(OUTPUT_FILE, index=False)\n",
    "\n",
    "print(\"IMDb data scraped and saved successfully!\")\n",
    "print(f\"Output file location: {OUTPUT_FILE}\")\n",
    "print(f\"Total records saved: {len(df)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7783c14d-0e43-4007-a084-fd86b27b47a1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (ml_env)",
   "language": "python",
   "name": "ml_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

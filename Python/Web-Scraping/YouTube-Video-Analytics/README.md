# YouTube Video Analytics (Web Scraping + NLP)

## Overview
This project scrapes publicly available video metadata from a YouTube
channel’s videos page and performs exploratory analysis, text processing,
and visualizations.

The project demonstrates:
- HTML-based data extraction from YouTube
- Data cleaning and transformation
- Natural Language Processing (NLP) on video titles
- Visual analytics and insights generation

## Data Source
- Public YouTube channel videos page
- Channel ID used for stability:
  https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ/videos

> Note: This project extracts embedded JSON data (`ytInitialData`) from the
> YouTube HTML page. Since YouTube frequently changes internal structures,
> the scraper may require updates in the future.

## Data Collected
- Video Title
- View Count
- Video Duration

## Data Processing
- View counts cleaned and converted to numeric values
- Durations normalized and categorized
- NLP applied on video titles:
  - Tokenization
  - Stopword removal
  - Stemming

## Visualizations
- WordCloud of video titles
- Top most viewed videos
- Distribution of videos by duration category

## Outputs
All generated outputs are stored in the `outputs/` directory:
- `youtube_videos.csv`
- `wordcloud_titles.png`
- `top_viewed_videos.png`
- `duration_category.png`

## Tools & Libraries
- Python
- Requests
- BeautifulSoup
- Pandas
- NLTK
- Matplotlib / Seaborn
- WordCloud

## Execution Mode
Jupyter Notebook (`youtube_video_analytics.ipynb`)

---

##  Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/YouTube-Video-Analytics.git
cd YouTube-Video-Analytics
pip install -r requirements.txt
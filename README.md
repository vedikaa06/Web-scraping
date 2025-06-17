# 📝 Quotes Scraper & Visualizer

A Python-based web scraper for [https://quotes.toscrape.com](https://quotes.toscrape.com) that extracts quotes, authors, and tags — then presents them visually in a clean, styled HTML page using static HTML and CSS.

---

## 📌 Features

- 🔍 Scrapes quotes, authors, and tags from the homepage.
- 🗃️ Saves the data as structured JSON (`quotes_data.json`).
- 🌐 Visualizes the quotes beautifully with `index.html`.
- 🧼 Clean modular code with `headers.py`, `scraping.py`, and reusable functions.
- 🧠 Fully commented for easy understanding and learning.

---

## 🖼️ Demo

📸 **Preview of Output HTML Page**

![docs:screenshot](https://github.com/user-attachments/assets/8c28263b-1859-4ef3-bea5-029fe0d97c63)


📂 [Open `index.html`](index.html) – view how quotes are rendered visually.

📄 Sample JSON Output

```json
{
  "quote": "“Try not to become a man of success. Rather become a man of value.”",
  "author": "Albert Einstein",
  "tags": ["adulthood", "success", "value"]
}

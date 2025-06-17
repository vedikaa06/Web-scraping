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
## 🚀 Deployed Website
You can view the live version of this project here:

👉 https://vedikaa06.github.io/Web-scraping/

This website is hosted using GitHub Pages and showcases the visual rendering of scraped quotes using only HTML and CSS.

📁 To view it locally, open index.html in your browser after running the scraper.

---

## 🖼️ Demo

📸 **Preview of Output HTML Page**

![docs:screenshot](https://github.com/user-attachments/assets/8c28263b-1859-4ef3-bea5-029fe0d97c63)


📂 [Open `index.html`](index.html) – view how quotes are rendered visually.

📥 [Download Full `quotes_data.json`](quotes_data.json)

---

## ⚙️ Installation Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/your-username/quotes-scraper.git
cd quotes-scraper
```
### ✅ 2. (Optional but Recommended) Create a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### ✅ 3. Install Dependencies
Install all required Python packages listed in requirements.txt:
```bash
pip install -r requirements.txt
```
💡 If you encounter issues with lxml, you can install it separately:
```bash
pip install lxml
```

### ✅ 4. Run the Scraper
Execute the scraper to fetch quotes from https://quotes.toscrape.com:
```bash
python scraping.py
```
This will extract the quotes, authors, and tags.

The output will be saved in a file called quotes_data.json.

### ✅ 5. View the Results in Browser
To view the quotes visually:

1. Open the index.html file in any modern web browser.
2. Browse and read quotes styled with a soft blue theme.
3. Optionally, download the JSON using the provided download link in the page.

---
## 📦 Project Structure
```bash
quotes-scraper/
│
├── scraping.py             # Main scraping script
├── headers.py              # Custom HTTP headers
├── quotes_data.json        # Output JSON file (auto-generated)
├── index.html              # Visual presentation of quotes
├── __init__.py             # Package initializer
├── .env                    # Optional environment variables
├── .gitignore              # Ignore unwanted files
├── requirements.txt        # Required Python libraries
└── docs/
    └── screenshot.png      # (Optional) Screenshot for demo
```
---

## 📋 Output Example
```json
{
  "quote": "“A day without sunshine is like, you know, night.”",
  "author": "Steve Martin",
  "tags": ["humor", "obvious", "simile"]
}
```

---
## 🛠️ Built With
Python 🐍

BeautifulSoup4

Requests

JSON

HTML + CSS (static styling)

---
## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request.

---
## 👤 Author
Vedika Agarwal
📧 vedikaa006@gmail.com

🌐 LinkedIn www.linkedin.com/in/vedika-agarwal-032909273



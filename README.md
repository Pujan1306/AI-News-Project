# 🧠 Gemini News Insight Generator

This Python project fetches the latest breaking news and uses **Google Gemini AI** to generate summaries, simple explanations, and Q&A insights. Ideal for news analysis, educational tools, or automation projects.

---

## 🚀 Features

- 📰 Fetches real-time breaking news using [NewsAPI](https://newsapi.org/)
- 🤖 Summarizes news content using [Google Gemini API](https://ai.google.dev/)
- 📘 Generates:
  - Simple explanations for better understanding
  - Concise summaries
  - Insightful Q&A based on the news
- 💾 Saves all enriched news to a local JSON file

---

## 🧠 How It Works

1. **Fetch News**
   - Pulls the latest headlines from NewsAPI
   - Stores them in a Python dictionary

2. **Gemini AI Processing**
   - Sends each article to Google Gemini AI
   - Receives structured output:
     - Summary
     - Simplified Explanation
     - Key Questions and Answers

3. **Save to JSON**
   - Saves enriched results to `news.json` for further use

---

## 🔧 Requirements

- Python 3.10+
- [Google Generative AI API key](https://ai.google.dev/)
- [NewsAPI key](https://newsapi.org/)
- `dotenv` package for managing API keys

---

## 🧪 Installation & Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/gemini-news-insight-generator.git
   cd gemini-news-insight-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file:**
   ```env
   NEWS_API_KEY=your_news_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the script:**
   ```bash
   python main.py
   ```

---

## 📁 Files Included

* `main.py` — Main script to run the news insight generator
* `news.py` — Handles fetching and saving news data
* `news.json` — Stores enriched AI-generated news insights
* `.env` — (Not included) Securely stores your API keys
* `requirements.txt` — List of required Python packages

---

## 📌 Notes

* Ensure you have a valid NewsAPI and Gemini API key.
* `news.json` will be overwritten on each run — back it up if needed.
* API limits may apply on free tiers — monitor usage accordingly.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Acknowledgements

* [NewsAPI](https://newsapi.org/)
* [Google AI Gemini](https://ai.google.dev/)
* [Python dotenv](https://pypi.org/project/python-dotenv/)

---

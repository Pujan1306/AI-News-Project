import google.generativeai as genai
import os
from dotenv import load_dotenv as loadenv
import json
from news import News


loadenv()

os.environ["GRPC_VERBOSITY"] = "NONE"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

news = News()
news.getNews()

with open('news.json', 'r') as file:
    data = json.load(file)

news_title = input("Enter News You Want To Search: ").strip()

if len(news_title) == 0:
    print("Please enter a valid news title.")
else:
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
You are a news filter bot. Given the following JSON array of articles: {data}

Search for the article with a title that closely matches this input:
Search Title: "{news_title}"

If a matching article is found (use a strict match or very close match on the title), then return:

- Title: (include the full title)
- Date: (in the format: YYYY-MM-DD)
- Link: (include the full URL)
- Description: (include the full description)

Then provide:
1. A simplified summary (max 50 words)
2. Why this news matters (in 1-2 lines)
3. Actionable insight: What should a student, investor, or professional do? (e.g., ignore, read more, invest, prepare, etc.)
4. Try to search for the latest news on this topic and return it.

If no matching article is found, just return:
"News Not Found"

Return ONLY the output in this format, no extra explanation.
"""

    
    response = model.generate_content(prompt)
    print(response.text)

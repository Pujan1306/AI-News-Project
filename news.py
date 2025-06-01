import requests
import os
from dotenv import load_dotenv as loadenv
import json

loadenv()

API_KEY = os.getenv("NEWS_API_KEY")
URL = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
class News:
    def __init__(self):
        self.URL = URL
        self.API_KEY = API_KEY
    def getNews(self):
        self.existing_articles = []
        if os.path.exists('news.json'):
            with open('news.json', 'r') as file:
                try:
                    self.existing_articles = json.load(file)
                except ValueError:
                    self.existing_articles = []
        self.existing_title = [article['title'] for article in self.existing_articles]
        self.existing_date = [article['Date'] for article in self.existing_articles]

        self.response = requests.get(self.URL)
        self.data = self.response.json()
        self.new_articles = []

        for self.new_article in self.data['articles']:
            if self.new_article['title'] not in self.existing_title and self.new_article['publishedAt'] not in self.existing_date:
                self.json_data = {
                'title': self.new_article['title'],
                'Date': self.new_article['publishedAt'],
                'url': self.new_article['url'],
                'description': self.new_article['description'],
                'content': self.new_article['content'] 
                }
                self.new_articles.append(self.json_data)

        if len(self.new_articles)>0:
            self.all_articles = self.existing_articles + self.new_articles
            try:
                with open('news.json', 'w') as file:
                    json.dump(self.all_articles, file, indent=4)
                    print("Articles saved to news.json")
            except Exception as e:
                print(f"Error writing to file: {e}")


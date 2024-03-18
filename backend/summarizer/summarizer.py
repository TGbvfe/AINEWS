import os
import json
import requests
from newsapi import NewsApiClient

# Initialize the NewsAPI client
newsapi = NewsApiClient(api_key='0060309c3ac44f6daa0245c75b842ba0')

# List of news sources
sources = ['wall-street-journal', 'cnn', 'cnbc', 'fox-news', 'bbc-news', 'nbc-news']

def get_articles():
    articles = []
    for source in sources:
        source_articles = newsapi.get_top_headlines(sources=source, language='en')['articles'][:5]
        for article in source_articles:
            article_data = {
                'content': article['content'],
                'title': article['title'],
                'url': article['url'],
                'author': article['author'] if 'author' in article else 'Unknown'
            }
            articles.append(article_data)
    return articles

def main():
    articles = get_articles()
    if articles:
        # Create the "New" folder if it doesn't exist
        os.makedirs('New', exist_ok=True)

        # Write the article information to news_store.json in the "New" folder
        article_data = {}
        for i, article in enumerate(articles, start=1):
            article_data[f'article{i}'] = {
                'content': article['content'],
                'title': article['title'],
                'url': article['url'],
                'author': article['author']
            }

        with open('New/news_store.json', 'w') as f:
            json.dump(article_data, f, indent=4)
        print("Article information stored in New/news_store.json")
    else:
        print("No articles found.")

if __name__ == "__main__":
    main()

import json
import requests

news_url = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=8bfdaf61cbd5499491b4f29de2ac696c')
news_data = news_url.json()
article = news_data['articles']
print(news_data['totalResults'])
num = news_data['totalResults']
print(len(article))
# with open('data.txt', 'w') as outfile:
#     json.dump(news_data, outfile)
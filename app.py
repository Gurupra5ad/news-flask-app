from flask import Flask, request, render_template
import requests
import json

app = Flask('__name__')

@app.route('/')
def index():
    api_key = '8bfdaf61cbd5499491b4f29de2ac696c'
    news_url = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=8bfdaf61cbd5499491b4f29de2ac696c')
    news_data = news_url.json()
    article = news_data['articles']
    number = len(article)
    return render_template('index.html',data = news_data,number=number)

from app import app
import urllib.request,json
from .models import news

News = news.News

#getting api key
api_key = app.config('NEWS_API_KEY')

#getting news base url
base_url = app.config('NEWS_API_BASE_URL')

def get_news():
    '''
    Function that gets the json from top headlines api
    '''
    get_news_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            
            news_results = process_results(news_results_list)
            
    return news_results

def process_results(news_list):
    '''
    Function that processes the news results and transfrms them into an object
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.author
        title = news_item.title
        description = news_item.description
        url = news_item.url
        urlToImage = news_item.urlToImage
        publishedAt = news_item.publishedAt
        content = news_item.content
        
    
            
from app import app
import urllib.request,json
from .models import news,sites,source,everything


News = news.News
Sites = sites.Sites
Source = source.Source
Everything = everything.Everything

#getting api key
api_key = 'fee3b3e955374e4e87747fef4b303740'

#getting news base url
base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

#evrything on news API
all_url = 'https://newsapi.org/v2/top-headlines?category={}&language=en&apiKey={}'

#sources on news API
source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

#getting all available news sources
sites_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'

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
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        
        news_object = News(author, title, description, url, urlToImage, publishedAt, content)
        
        news_results.append(news_object)
    return news_results



def get_sites():
    '''
    Function that gets the json from all available sites from newsAPI
    '''
    get_sites_url = sites_url.format(api_key)
    
    with urllib.request.urlopen(get_sites_url) as url:
        get_sites_data = url.read()
        get_sites_response = json.loads(get_sites_data)
        
        sites_results = None
        
        if get_sites_response['sources']:
            sites_results_list = get_sites_response['sources']
            
            sites_results = process_results(sites_results_list)
            
    return sites_results

def process_results(sites_list):
    '''
    Function that processes the sources results and transfrms them into an object
    '''
    sites_results = []
    for site_item in sites_list:
        id = site_item.get('id')
        name = site_item.get('name')
        description = site_item.get('description')
        url = site_item.get('url')
        category = site_item.get('category')
        language = site_item.get('language')
        country = site_item.get('country')
        
        
        sites_object = Sites(id,name,description,url,category,language,country)
        
        sites_results.append(sites_object)
    return sites_results
        
    
            
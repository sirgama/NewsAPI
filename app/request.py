from app import app
import urllib.request,json
from .models import News, Sites, Source, Everything


# News = news.News
# Sites = sites.Sites
# Source = source.Source
# Everything = everything.Everything

#getting api key
api_key = 'fee3b3e955374e4e87747fef4b303740'

#getting news base url
base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

#evrything on news API
all_url = 'https://newsapi.org/v2/top-headlines?category={}&language=en&apiKey={}'

#sources on news API
source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

#getting all available news sources
sites_url = 'https://newsapi.org/v2/top-headlines/sources?language=en&apiKey={}'

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
        
        if urlToImage:
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
        
        if get_sites_response["sources"]:
            sites_results_list = get_sites_response["sources"];
            
            sites_results = process_sites(sites_results_list)
            
    return sites_results

def process_sites(sites_list):
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
        
        
        site_object = Sites(id, name, description, url, category, language, country)
        
        sites_results.append(site_object)
    return sites_results
        

def get_source(name):
    '''
    Function that gets the json from all available sites from newsAPI
    '''
    get_sources_url = source_url.format(name,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_results = None
        
        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            
            sources_results = process_results(sources_results_list)
            
    return sources_results

def process_results(sources_list):
    '''
    Function that processes the sources results and transfrms them into an object
    '''
    sources_results = []
    for source_item in sources_list:
        source = source_item.get('source')
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')
        content = source_item.get('content')
        
        if urlToImage:
            sources_object = Source(source,author,title,description,url,urlToImage,publishedAt,content)
            
            sources_results.append(sources_object)
    return sources_results



def get_everything(category):
    '''
    Function that gets the json from all available sites from newsAPI
    '''
    get_everything_url = all_url.format(category,api_key)
    
    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)
        
        everything_results = None
        
        if get_everything_response['articles']:
            everything_results_list = get_everything_response['articles']
            
            everything_results = process_results(everything_results_list)
            
    return everything_results

def process_results(everything_list):
    '''
    Function that processes the sources results and transfrms them into an object
    '''
    everything_results = []
    for source_item in everything_list:
        
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')
        content = source_item.get('content')
        
        if urlToImage:
            everything_object = Everything(author,title,description,url,urlToImage,publishedAt)
            
            everything_results.append(everything_object)
    return everything_results
    
            
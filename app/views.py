from flask import render_template
from app import app
from .request import get_news, get_sites, get_source

#Views for the app

@app.route('/')
def index():
    '''
    returns the index page
    '''
    
    sites = get_sites()
    news = get_news()
    message = 'Testing the news site'
    return render_template('index.html', message= message, channels=sites, updates = news)

@app.route('/source/<name>')
def source(name):
    
    '''
    returns the source page
    '''
    
    sources = get_source(name)
    heading = name.upper()
    return render_template('source.html', medias=sources, head= heading)

@app.route('/everything')
def everything():
    
    return render_template('everything.html')
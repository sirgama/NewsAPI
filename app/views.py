from flask import render_template
from app import app
from .request import get_news, get_sites, get_source

#Views for the app

@app.route('/')
def index():
    '''
    returns the index page
    '''
    news = get_news()
    sites = get_sites()
    sources = get_source()
    message = 'Testing the news site'
    return render_template('index.html', message= message, articles= news ,channels = sites, medias = sources)

@app.route('/source/<int:source>')
def source(source):
    
    '''
    returns the source page
    '''
    return render_template('source.html' )
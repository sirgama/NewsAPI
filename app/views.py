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
    
    message = 'Testing the news site'
    return render_template('index.html', message= message,channels = sites)

@app.route('/source/<name>')
def source(name):
    
    '''
    returns the source page
    '''
    sites = get_sites()
    sources = get_source(name)
    return render_template('source.html', medias=sources, channels = sites )
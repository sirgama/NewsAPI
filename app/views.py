from flask import render_template
from app import app
from .request import get_news, get_sites

#Views for the app

@app.route('/')
def index():
    '''
    returns the index page
    '''
    news = get_news()
    sites = get_sites()
    message = 'Testing the news site'
    return render_template('index.html', message= message, articles= news ,channels = sites)

@app.route('/article/<int:id>')
def article(id):
    
    '''
    returns the article page
    '''
    return render_template('article.html' )
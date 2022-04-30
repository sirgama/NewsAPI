from flask import render_template
from app import app

#Views for the app

@app.route('/')
def index():
    '''
    returns the index page
    '''
    message = 'Testing the news site'
    return render_template('index.html', message= message)

@app.route('/article/<int:id>')
def article(id):
    
    '''
    returns the article page
    '''
    return render_template('article.html' )
from flask import render_template
from app import app
from .request import get_everything, get_news, get_sites, get_source

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

@app.route('/business')
def business():
    
    businesses = get_everything('business')
    return render_template('business.html', businesses=businesses)

@app.route('/technology')
def technology():
    
    technologies = get_everything('technology')
    return render_template('technology.html', technologies=technologies)

@app.route('/entertainment')
def entertainment():
    
    entertainments = get_everything('entertainment')
    return render_template('entertainment.html',entertainments = entertainments)

@app.route('/sports')
def sports():
    
    sports = get_everything('sports')
    return render_template('sports.html', sports =sports)

@app.route('/science')
def science():
    
    sciences = get_everything('science') 
    return render_template('science.html', sciences = sciences)
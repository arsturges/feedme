from flask import Flask, render_template, url_for
from yelp_api2 import yelp_api2
from google_maps_api import google_maps_api

app = Flask(__name__)
app.debug = True # Set to false before deploying!
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('home.html', title = "Home", yelp_api2=yelp_api2)

@app.route('/pods')
def pods():
    return render_template('pods.html', title = "Pods") 

@app.route('/map')
def map():
    return render_template('map.html', title = "Map", google_maps_api=google_maps_api) 

@app.route('/trucks')
def trucks():
    return render_template('trucks.html', title = "Trucks") 

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html', title = "Restaurants") 

@app.route('/help')
def help():
    return render_template('help.html', title = "Help") 

@app.route('/about')
def about():
    return render_template('about.html', title = "About", google_maps_api=google_maps_api) 

@app.route('/contact')
def contact():
    return render_template('contact.html', title = "Contact") 

if __name__ == '__main__':
    app.run() #host='0.0.0.0',port=80) #disable app.debug before pushing to production.
    print google_maps_api['api_key']
    print 'andrew'

from flask import Flask, render_template, url_for
import yelp_api2

app = Flask(__name__)
app.debug = True # Set to false before deploying!
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('home.html', title = "Home", yelp_api2=yelp_api2)

@app.route('/help')
def help():
    return render_template('help.html', title = "Help") 

@app.route('/about')
def about():
    return render_template('about.html', title = "About") 

@app.route('/contact')
def contact():
    return render_template('contact.html', title = "Contact") 

if __name__ == '__main__':
    app.run() #host='0.0.0.0',port=80) #disable app.debug before pushing to production.

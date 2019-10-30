from flask import Flask, render_template #import Flask variable from the flask package
# from flask import render_template
# Flask variable is an object
# an object contains 2 things -- data and functionality
import os

app = Flask(__name__) # __name__ is a special Python variable

@app.route('/') # set up a route
def hello():
    name = "Paul"
    return render_template('index.template.html', n=name)
    
@app.route('/about') # route the /about url to the about_page function
def about_page():
    return "<h1>About Us</h1>"
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

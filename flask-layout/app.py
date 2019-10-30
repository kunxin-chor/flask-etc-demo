from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

#Begin routes here

@app.route('/')
def index():
    return render_template('index.template.html')


@app.route('/about-us')
def about_us():
    return render_template('about_us.template.html')

@app.route('/our-animals')
def our_animals():
    return render_template('animals.template.html')

#End routes here

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
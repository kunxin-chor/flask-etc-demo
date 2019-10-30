from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.template.html')

@app.route("/login", methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']
    

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    all_fruits = ['Apple', 'Mango', 'Orange',  'Banana', 'Durian', 'Rambutan']
    selected = ['Apple', 'Banana']
    selected_single_fruit = 'Banana'
    return render_template('index.template.html',
    selected_fruits = selected, all_fruits=all_fruits, selected_single_fruit=selected_single_fruit)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
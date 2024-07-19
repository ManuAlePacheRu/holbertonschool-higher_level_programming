#!/usr/bin/python3

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data_item = json.load(file)
    if data_item:
        items_lis = data_item["items"]
    else:
        items_lis = []
    return render_template('items.html', items=items_lis)

if __name__ == '__main__':
   app.run(debug=True, port=5000)

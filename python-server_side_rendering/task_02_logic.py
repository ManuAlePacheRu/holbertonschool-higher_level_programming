from flask import Flask, render_template
import jinja2
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
   with open("items.json") as list_items:
        items_data = json.load(list_items)   

   if items_data:
      items_py = items_data["items"]
   else:
      items_py = []
   return render_template('items.html', items_py=items)

if __name__ == '__main__':
   app.run(debug=True, port=5000)

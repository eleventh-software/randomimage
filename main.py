import requests
from flask import Flask, request, render_template, url_for, flash, redirect, session
app = Flask(__name__)

api_key = 'y29T738F4iwHyvBjauMBJJ5wUGzQ3vqS4VxV1FxNNl8'
api_url = 'https://api.unsplash.com'

@app.route('/', methods=['GET', 'POST'])
def home():
    data  = getrandom()
    return render_template('index.html', data=data)

def getrandom():
    r = requests.get(f"https://api.unsplash.com/photos/random?client_id={api_key}")
    data = r.json()
    return data
    
    
if __name__ == "__main__":
    app.run(debug=True)
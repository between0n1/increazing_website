from flask import Flask
from classes import *



app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to my Flask WebSite"
if __name__ == '__main__':
    app.run()
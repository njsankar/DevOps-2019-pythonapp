import os
from flask import Flask
from app import word_generator

app = Flask(__name__)

@app.route("/")
def generate_sentence():
    page = '<html><body><h1>'
    page += word_generator.generate_sentence()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
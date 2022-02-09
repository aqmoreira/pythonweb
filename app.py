from flask import Flask

app = Flask("Hello")

@app.route('/home')
def home():
    return "Hello from Flask"


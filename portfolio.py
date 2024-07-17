import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

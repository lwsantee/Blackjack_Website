from flask import redirect, render_template, request, url_for
from blackjack import app


@app.route('/')
def index():
    return render_template('index.html')

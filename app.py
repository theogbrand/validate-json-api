# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello(name=None):
  
  return "Hello, yo!"


#!/usr/bin/env python3
"""Simple Flask App module"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('0-index.html')

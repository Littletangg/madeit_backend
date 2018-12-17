# encoding=utf-8
from flask import Flask, jsonify, current_app, request
import sqlite3
from datetime import date,datetime
import os.path,json, sys
from modal import QA, Card, Category
from flask_sqlalchemy import SQLAlchemy
from langdetect import detect
import string

app = Flask(__name__)
app.logger.error(str(os.path.dirname(__file__)))
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
if basedir not in sys.path:
    sys.path.insert(0, basedir)

app.logger.error(str(basedir))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/db/%s.sqlite3' % (basedir, "madeit")
app.logger.error(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

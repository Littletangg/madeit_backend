import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/db/%s.sqlite3' % (basedir, "madeit_db")
# print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(25), default="user", nullable=False)
    role_description = db.Column(db.Text)

    def __repr__(self):
        return '<Role %r>' % self.role_name

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(125), unique=True, nullable=False)
    team_lead_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Team %r>' % self.team_name

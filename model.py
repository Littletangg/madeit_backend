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
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(25), default="user", nullable=False)
    role_description = db.Column(db.Text)

    def __repr__(self):
        return '<Role %r>' % self.role_name

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(125), unique=True, nullable=False)
    team_lead_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Team %r>' % self.team_name

class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, unique=True)

    # relationships ------------------------------
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    team = db.relationship("Team")

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    employee = db.relationship("Employee")

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("Role")

    def __repr__(self):
        return '<TeamMember id %r>' % self.id

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(125), nullable=False)
    first_name = db.Column(db.String(125), nullable=False)
    last_name = db.Column(db.String(125), nullable=False)
    nick_name = db.Column(db.String(80))
    employee_level = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(225))

    # relationships ------------------------------
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    team = db.relationship("Team")

    def __repr__(self):
        return '<Employee %r>' % self.username

class EmployeeSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    progress = db.Column(db.Integer)

    # relationships ------------------------------
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))
    skill = db.relationship("Skill")

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))
    employee = db.relationship("Employee")

    def __repr__(self):
        return '<EmployeeSkill id %r>' % self.id



    










     

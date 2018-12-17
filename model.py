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

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(225), unique=True, nullable=False)
    skill_description = db.Column(db.Text)

    def __repr__(self):
        return '<Skill %r>' % self.skill_name

class GoalPromote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    next_position_id = db.Column(db.Text, default='[]')
    target = db.Column(db.Text, default='[]')

    # relationships ------------------------------
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.id"))
    skill = db.relationship("Skill")

    position_id = db.Column(db.Integer, db.ForeignKey("position.id"))
    position = db.relationship("Position")

    def __repr__(self):
        return '<GoalPromote id %r>' % self.id

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(225), unique=True, nullable=False)
    position_description = db.Column(db.Text)

    def __repr__(self):
        return '<Position %r>' % self.position_name

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(225), unique=True, nullable=False)
    project_description = db.Column(db.Text)
    project_manager = db.Column(db.Integer)  #employee id of PM
    start_date = db.Column(db.DateTime, default=datetime.now)
    end_date = db.Column(db.DateTime, default=datetime.now)
    customer = db.Column(db.String(225))

    def __repr__(self):
        return '<Project %r>' % self.project_name

class ProjectMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Text, default='[]') #JSON of member id

    # relationships ------------------------------
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    project = db.relationship("Project")
    
    def __repr__(self):
        return '<ProjectMember %r>' % self.id

class KR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_description = db.Column(db.Text) 
    key_value = db.Column(db.Integer)   #the progress of this KR
    key_unit = db.Column(db.Integer)    #the weight of this KR

    # relationships ------------------------------
    objective_id = db.Column(db.Integer, db.ForeignKey("objective.id"))
    objective = db.relationship("Objective")

    def __repr__(self):
        return '<KR id %r>' % self.id

class Objective(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    objective_type = db.Column(db.String(225))
    objective_title = db.Column(db.String(225), nullable=False)
    objective_description = db.Column(db.Text) 
    # status = db.Column(db.Integer)
 
    def __repr__(self):
        return '<Objective %r>' % self.id

# class ObjectiveTeam(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     objective_title = db.Column(db.String(225), nullable=False)
#     objective_description = db.Column(db.Text) \
#     status = db.Column(db.Integer)

#     # relationships ------------------------------
#     objective_id = db.Column(db.Integer, db.ForeignKey("objective.id"))
#     objective = db.relationship("Objective")

#     def __repr__(self):
#        return '<ObjectiveTeam %r>' % self.id

# class ObjectiveCompany(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     objective_title = db.Column(db.String(225), nullable=False)
#     objective_description = db.Column(db.Text) \
#     status = db.Column(db.Integer)

#     # relationships ------------------------------
#     objective_id = db.Column(db.Integer, db.ForeignKey("objective.id"))
#     objective = db.relationship("Objective")

#     def __repr__(self):
#        return '<ObjectiveCompany %r>' % self.id

# class ObjectivePersonal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     objective_title = db.Column(db.String(225), nullable=False)
#     objective_description = db.Column(db.Text) \
#     status = db.Column(db.Integer)

#     # relationships ------------------------------
#     objective_id = db.Column(db.Integer, db.ForeignKey("objective.id"))
#     objective = db.relationship("Objective")

#     def __repr__(self):
#        return '<ObjectivePersonal %r>' % self.id
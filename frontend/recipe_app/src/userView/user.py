import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

############################################################################################################

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "data.db"))
userApp = Flask(__name__)
userApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(userApp)

class Users(db.Model):
    __tablename__ = 'user_data'
    username = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    type = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
            return "<Username: {}\tPassword: {}\tType: {}>".format(self.username, self.password, self.type)


############################################################################################################
@userApp.route('/')
def index():
    return render_template('index.html')

@userApp.route("/data", methods=["GET","POST"])
def addUser():
    if request.form:
        username = request.form.get("username")
        user = Users.query.filter_by(username=username).first()
        if user:
            return "Username already exists. Please provide a unique username."
        
        user = Users(username=request.form.get("username"),
                    password=request.form.get("password"),
                    type=request.form.get("type"))
        db.session.add(user)
        db.session.commit()
    users = Users.query.all()
    return render_template("userData.html", users=users)

############################################################################################################

@userApp.route("/data/update", methods=["POST"])
def updateUser():
    newUsername = request.form.get("newUsername")
    newPassword = request.form.get("newPassword")
    newType = request.form.get("newType")

    user = Users.query.filter_by(username=newUsername).first()
    user.password = newPassword
    user.type = newType
    db.session.commit()
    return redirect("/data")

############################################################################################################

@userApp.route("/data/delete", methods=["POST"])
def deleteStudent():
    delete_user = request.form.get("delete_user")
    user = Users.query.filter_by(username=delete_user).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/data")

if __name__ == "__main__":
    userApp.run()
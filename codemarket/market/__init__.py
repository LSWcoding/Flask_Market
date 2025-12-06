from flask import Flask#import the flask framework
from flask_sqlalchemy import SQLAlchemy#import the sqlalchemy database
from flask_bcrypt import Bcrypt#import the Bcrypt to encrypt the password input
from flask_login import LoginManager#to provide some function for login

app = Flask(__name__)#to create a flask app object to take advantages of flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'#to tell flask where to create database
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'#to encrypt and secure session
db = SQLAlchemy(app)#create a database object with flask app
bcrypt = Bcrypt(app)#create a Bcrypt object with flask app then implement security
login_manager = LoginManager(app)#create a LoginManager object with flask app to implement login function
login_manager.login_view = "login_page"#to define that to redirect to login_page when accessing the page where @login_required is written
login_manager.login_message_category = "info"#"info" is one of the login_message_category,the content in "info" shows up when accessing pages decorated by @login_required
from market import routes#routes must be imported at the button of __init__ file
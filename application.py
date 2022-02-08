import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://haletfdvshzpjr:a581b8c4aeae076d1284a1fddfe9f28df4fc620fe999410f86f18713a0ccf796@ec2-54-224-194-214.compute-1.amazonaws.com:5432/d2bfh6ims5dms6' #os.getenv("DATABSE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/form")
def form():
    return "success!"


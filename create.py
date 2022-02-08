import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://haletfdvshzpjr:a581b8c4aeae076d1284a1fddfe9f28df4fc620fe999410f86f18713a0ccf796@ec2-54-224-194-214.compute-1.amazonaws.com:5432/d2bfh6ims5dms6' #os.getenv("DATABSE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()

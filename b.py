from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

print("Connected to MongoDB successfully!")

# ... rest of your Flask code
@app.route('/check_db_connection')
def check_db_connection():
    collection = mongo.db.your_collection_name  # Replace with your actual collection name
    document = collection.find_one()
    return f"Connection to MongoDB established. Found document: {document}"


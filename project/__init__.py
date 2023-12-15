from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from flask_cors import CORS
flask_app = Flask(__name__)
api = Api(flask_app)
cors = CORS(flask_app, resources={r'*': {"origins": '*'}})


client = MongoClient("mongodb://localhost:27017/SocialMedia")
db = client['SocialMedia']
collection = db['Posts']


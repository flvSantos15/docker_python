from flask import Flask, request

from src import UserRepository

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/insert", methods=["POST"])
def insert_user():
  user_repository = UserRepository()
  body = request.get_json()
  
  name = body["name"]
  user_repository.insert_user(name)
  
  return "User inserted"
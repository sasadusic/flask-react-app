from app import app, db
from flask import request, jsonify
from models import Friend

# Get all friends
@app.route('/api/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result)
    # return "<h1 style='font-family: sans-serif;'>Flask React App</h1>"

@app.route('/api/friends', methods=["POST"])
def create_friend():
    try:
        data = request.json

        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")
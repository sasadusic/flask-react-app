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

        # Fetch avatar imagr based on gender
        if gender == "male":
            img_url = f"https://avatar.iran.ilara.run/public.boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.ilara.run/public.?username={name}"
        else:
            img_url = None

        new_friend = Friend(name=name, role=role, description=description, gender=gender, img_url=img_url)

        db.session.add(new_friend)
        db.session.commit()

        # return jsonify(new_friend.to_json()), 201
        return jsonify({"msg": "Fr  iend created successfuly"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 500
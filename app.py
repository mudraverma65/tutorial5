from flask import Flask, jsonify, request

app = Flask(__name__)

class User:
    def __init__(self, email, firstName, id):
        self.email = email
        self.firstName = firstName
        self.id = id

listOfUsers = []

user1 = User("abc@abc.ca", "ABC", "1")
user2 = User("xyz@xyz.ca", "XYZ", "2")

listOfUsers.append(user1)
listOfUsers.append(user2)

@app.route('/users', methods=['GET'])
def getMethod():
    response = {
        "message": "Users retrieved",
        "success": True,
        "users": [user.__dict__ for user in listOfUsers]
    }
    return jsonify(response)

@app.route('/update/<string:user_id>', methods=['PUT'])
def updateMethod(user_id):
    data = request.get_json()
    for user in listOfUsers:
        if user.id == user_id:
            if 'email' in data:
                user.email = data['email']
            if 'firstName' in data:
                user.firstName = data['firstName']
            response = {
                "message": "User updated",
                "success": True
            }
            return jsonify(response)
    response = {
        "message": "User not found",
        "success": False
    }
    return jsonify(response), 404

@app.route('/add', methods=['POST'])
def addMethod():
    data = request.get_json()
    email = data.get('email')
    firstName = data.get('firstName')

    if not email or not firstName:
        response = {
            "message": "Email and firstName are required fields",
            "success": False
        }
        return jsonify(response), 400

    user_id = str(len(listOfUsers) + 1)
    new_user = User(email, firstName, user_id)
    listOfUsers.append(new_user)
    response = {
        "message": "User added",
        "success": True
    }
    return jsonify(response), 201

@app.route('/user/<string:user_id>', methods=['GET'])
def getUserMethod(user_id):
    for user in listOfUsers:
        if user.id == user_id:
            response = {
                "success": True,
                "user": user.__dict__
            }
            return jsonify(response)
    response = {
        "message": "User not found",
        "success": False
    }
    return jsonify(response), 404

@app.errorhandler(400)
def bad_request(error):
    response = {
        "message": "Bad Request",
        "success": False
    }
    return jsonify(response), 400

@app.errorhandler(500)
def server_error(error):
    response = {
        "message": "Internal Server Error",
        "success": False
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

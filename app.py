from flask import Flask, jsonify

app = Flask(__name__)

class User:
    def __init__(self, email, firstName, id):
        self.email = email
        self.firstName = firstName
        self.id = id

listOfUsers = []

user1 = User("abc@abc.ca", "ABC", "5abf6783")
user2 = User("xyz@xyz.ca", "XYZ", "5abf674563")

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

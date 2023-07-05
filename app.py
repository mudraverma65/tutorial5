from flask import Flask,request
import json

app = Flask(__name__)

class User:
    def __init__(self,userName, email):
        self.userName = userName
        self.email = email

listOfUsers = []

user1 = User("user1","user1@gmail.com")
user2 = User("user2","user2@gmail.com")

listOfUsers.append(user1)
listOfUsers.append(user2)

@app.route('/getMethod', methods=['GET'])
def getMethod():
    jsonList = json.dumps([ob.__dict__ for ob in listOfUsers])
    return jsonList

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
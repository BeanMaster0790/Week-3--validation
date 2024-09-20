from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

userList = ["123"]

@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")

@app.route("/alterlist", methods=["POST"])
def alterList():

    data = request.get_json()
    number = data.get('number')

    option = data.get("option")

    if(option == "add"):
        addUser(userList, number)
    if(option == "remove"):
        removeUser(userList, number)
    if(option == "exist"):
        return jsonify({"message": doesExist(userList, number)})

    return jsonify({"message": userList})

def addUser(userList, user):

    userList.append(user)

    return userList

def removeUser(userList, user):

    userList.remove(user)

    return userList

def doesExist(userList, user):

    return (user in userList)

app.run()
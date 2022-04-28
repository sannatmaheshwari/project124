from asyncio import Task
import json
from flask import Flask,jsonify,request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Raju',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rahul',
        'Contact': u'9876543222', 
        'done': False
    }
]

@app.route("/")
def hello():
    return "hello world"

@app.route("/get-data")
def getTask():
    return jsonify({
        "data":List
    })

@app.route("/go",methods = ["POST"])
def sendData():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    task = {
        "id":List[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json["Contact"],
        "done":False
    } 
    List.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })



if(__name__=="__main__"):
    app.run(debug = True)
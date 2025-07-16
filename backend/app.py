from flask import Flask,request,render_template,jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)


@app.route("/submit",methods=['post'])

def submit():
    form_data = dict(request.json)
    print(form_data)
    collection.insert_one(form_data)
    return "Data submitted successfully"

@app.route("/view")

def view():
    data = collection.find()
    data = list(data)
    for i in data:
        del i['_id']
    data = {
        'data':data
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000, debug=True)
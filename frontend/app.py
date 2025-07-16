from flask import Flask,render_template,request
from datetime import datetime
import requests

BACKEND_URL='http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')

def home():
    time = datetime.now()
    return render_template('index.html',current_time= str(time.strftime("%d/%m/%y")),day= str(time.strftime("%A")))

@app.route("/submit",methods=['post'])

def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit',json=form_data)
    return "Data submitted successfully"

@app.route('/api')
def get_data():
    response = requests.get(BACKEND_URL+'/view')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
from flask import Flask, render_template,jsonify,request
from pymongo import MongoClient
import socket

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["userID_db"]
    return db

@app.route('/')
def pingserver():
    return f"Welcome to the world of animals, From Your Container : {socket.gethostname()}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    db=""
    error = None
    Details =None
    flag=0
    if request.method == 'POST':
        usname = request.form['username']
        passd = request.form['password']
        try:
            db = get_db()
            _users = db.userID_tb.find()
            for user in _users:
                if user["name"]==usname and user["password"]==passd:
                    studDetails = [{"id": user["id"], "name": user["name"], "branch": user["branch"]}]
                    Details = jsonify({"Details":studDetails})
                    flag=1
                    break
        except:
            pass
        finally:
            if type(db)==MongoClient:
                db.close()
        if flag==1:
            return Details
        else:
            error = "Please try again!"
    return render_template('login.html', error=error)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
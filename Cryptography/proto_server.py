import requests
import hashlib as hs
import mysql.connector as mysql

from flask import Flask, render_template, request

app=Flask(__name__)

def connect():
    
    return mysql.connect(host = "localhost", user = "auth_server", password = "password", database = "ident_info")

# @app.route('/login', methods = ['POST'])
# def log_in():
    
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)


@app.route('/identification', methods = ['GET'])
def ident():
    
    print("Enter login: ")
    login = input()
    print("Enter password: ")
    password = input()
    
    loghash = hs.sha256()
    loghash.update(login.encode('utf8'))
    logdigest = loghash.hexdigest()
    
    passhash = hs.sha256()
    passhash.update(password.encode('utf8'))
    passdigest = passhash.hexdigest()
    
    db = connect()
    add = db.cursor()
    add.execute("INSERT INTO LogPass (login, password) VALUES (%s, %s)", (logdigest, passdigest))
    db.commit()
    
    return "User created"


@app.route('/authentification', methods = ['GET'])
def auth():
    
    isValid = None 
    
    login = request.form['Login']
    password = request.form['Password']
    
    loghash=hs.sha256()
    loghash.update(login.encode('utf8'))
    logdigest=str(loghash.hexdigest())
    
    passhash=hs.sha256()
    passhash.update(password.encode('utf8'))    
    passdigest=str(passhash.hexdigest())
    
    db = connect()
    add = db.cursor()
    add.execute("SELECT * FROM LogPass WHERE login=%s and password=%s", (logdigest, passdigest))
    log = add.fetchall()
    
    if len(log) != 1:
        isValid = "Access denied. Wrong password and/or login."
    
    else:
        fetch = log[0]
        if len(fetch) != 3:
            return "Invalid row"
    
        if fetch[1] == logdigest and fetch[2] == passdigest:
            isValid = "Access granted"
        
        else:
            isValid = "Access denied. Wrong password and/or login."
    
    return isValid



if __name__ == "__main__":
    
    app.run(host = '0.0.0.0', port = 5555)
'''
Created on 2016. 4. 11.

@author: David
'''
# -*- coding: cp949 -*-
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flaskext.mysql import MySQL

#for test
from Person import Person
import login_check

#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.config['SECRET_KEY'] = 'secret2!'

mysql.init_app(app)
io = SocketIO(app)

def login_checks(email, pw):
    conn = mysql.connect()
    cursor = conn.cursor()
     
    query = "SELECT user_name FROM user_table WHERE user_username = %s AND user_pw = %s"
    value = (email, pw)
    cursor.execute(query, value)
    data = cursor.fetchall()
     
    cursor.close()
    conn.close()
     
    if data:
        return 1
    else:
        return 0

@app.route("/")
def main():
    #return 'Welcome'
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

#Got message from socket.io client emit
@io.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@app.route('/signUp', methods=['POST'])
def signUp():
    
    # create user code will be here !!
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    
    print _name + ', ' + _email + ', ' + _password
    
    lc = login_check
    lc.login.ch(_email, _password)

    result = login_checks(_email, _password)
    
    if result:
        io.emit('my_response', 'data')
    else:
        io.emit('my_response', 'not data')
    
#     query = "insert into user_table(user_name, user_username, user_pw) values(%s, %s, %s)"
#     values = (_name, _email, _password)
#      
#     cursor.execute(query, values)
#     conn.commit()
#     
#     print data
#     
#     cursor.close()
#     conn.close()
    
    #emit('my_response', "Oh yes!", broadcast=True)
    #_hashed_password = generate_password_hash(_password)
    
    

if __name__ == "__main__":    
    io.run(app)
    #app.run()
    

'''
Created on 2016. 4. 11.

@author: David
'''
from flask import Flask, render_template, request, json
from flask_socketio import SocketIO
from flaskext.mysql import MySQL

#for test
from Person import Person

#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'python'
app.config['MYSQL_DATABASE_HOST'] = '0.0.0.0'

app.config['SECRET_KEY'] = 'secret!'

mysql.init_app(app)
io = SocketIO(app)


@app.route("/")
def main():
    #return 'Welcome'
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


if __name__ == "__main__":    
    io.run(app, host='0.0.0.0', port=50000)
    #app.run()
    

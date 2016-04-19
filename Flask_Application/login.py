# -*- coding: utf8 -*-
import os
import sys
from datetime import datetime
from flask import Flask, request, render_template, flash, json
from werkzeug import redirect, secure_filename
from flask.helpers import url_for, make_response
from flask_mail import Mail, Message
from elasticsearch import Elasticsearch
import MySQLdb as mysql

# import flask module
app = Flask(__name__)

es = Elasticsearch();
app.secret_key = 'secret'

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['post', 'get'])
def login():
    error = None
    if request.method == 'POST':
        
        email = request.form['email']
        pw = request.form['pw']
        
        conn = mysql.connect(host='localhost', user='root', passwd='admin', db='python', charset='utf8')
        cursor = conn.cursor()
         
        query = "SELECT user_name FROM user_table WHERE user_email = %s AND user_pw = %s"
        value = (email, pw)
        cursor.execute("set names utf8")
        cursor.execute(query, value)
        data = (cursor.fetchall())
        
        cursor.close()
        conn.close()
        
        for row in data:
            data = row[0]
        
        if data:
            print 'login success'
            return redirect(url_for('success', name=data))
        else:
            error = 'Invalid input data detected!'
            
        #return redirect(url_for('success', name=user))
    
    return render_template('python_login.html', error=error)

@app.route('/regist', methods=['post', 'get'])
def regist():
    error = None
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        pw = request.form['pw']
        
        print name, email, pw
        
        conn = mysql.connect(host='localhost', user='root', passwd='admin', db='python', charset='utf8')
        cursor = conn.cursor()
        
        query = "SELECT 1 FROM user_table WHERE user_email = '%s' " % (email)
        #value = (email)
        cursor.execute(query)
        data = cursor.fetchall()
        
        if data:
            print 'user other email'
            error = "The email is already used. please use another one"
        else:
            print 'use it okay'
            query = "INSERT INTO user_table (user_name, user_email, user_pw) values (%s, %s, %s)"
            value = (name, email, pw)
            cursor.execute(query, value)
            data = cursor.fetchall()
            print data
            if not data:
                conn.commit()
                print data
                return "Register Success"
            else:
                conn.rollback()
                print data
                return "Register Failed"
        
        
        cursor.close()
        conn.close()

    return render_template('python_regist.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
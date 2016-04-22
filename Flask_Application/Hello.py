# -*- coding: utf-8 -*-
import os, datetime
from flask import Flask, render_template, flash, jsonify, request
from werkzeug import redirect, secure_filename
from flask.helpers import url_for, make_response
from flask_mail import Mail, Message
from functools import wraps, update_wrapper
from elasticsearch import Elasticsearch
import MySQLdb as mysql
from matplotlib.pyplot import plot, title, legend, show
from scipy import stats, polyval


# import flask module
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yu.david880'
app.config['MAIL_PASSWORD'] = 'Qkswl6100'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


#app.config['']

app.secret_key = 'secret'

@app.route('/machine', methods=['post', 'get'])
def machine():
    x = [3.52, 2.58, 3.31, 4.07, 4.62, 3.98, 4.29, 4.83, 3.71, 4.61, 3.90, 3.20]
    y = [2.48, 2.27, 2.47, 2.77, 2.98, 3.05, 3.18, 3.46, 3.03, 3.25, 2.67, 2.53]
    
    slope, intercept, r_value, p_value, stderr = stats.linregress(x, y)
    
    ry = polyval([slope, intercept], x)
    
    print ry
    
    plot(x, y, 'k.')
    
    plot(x, ry, 'r.-')
    
    title('Regression result')
    
    legend(['original', 'regression'])
    
    show()
    
    return 'ok'

@app.route('/music', methods=['post', 'get'])
def music_play():
    if request.method == 'POST':
            conn = mysql.connect(host='localhost', user='root', passwd='admin', db='python', charset='utf8')
            cursor = conn.cursor()
             
            query = "SELECT st, et, lyrics FROM lyrics " # WHERE user_email = %s AND user_pw = %s
            #value = (email, pw)
            #cursor.execute("set names utf8")
            cursor.execute(query)
            data = cursor.fetchall()

            cursor.close()
            conn.close()
#             return list(data)
            return jsonify(info = data)
    
    else:
        return render_template('music.html')

@app.route('/facebook', methods=['post', 'get'])    
def facebook_data():
    es = Elasticsearch();
    #data = es.search(index='facebook', doc_type='fb')
    sizes = 20 #data['hits']['total']
    data = es.search(index='facebook', size=sizes)
    
    g_list=[]
    for hit in data['hits']['hits']:
        g_list.append({'message':hit['_source']['message'], 'created_time':hit['_source']['created_time']})
        
    return render_template('facebook.html', content = g_list)

@app.route("/email", methods=['post', 'get'])
def email_test():
    
    if request.method == 'POST':
        senders = request.form['email_sender']
        receiver = request.form['email_receiver']
        content = request.form['email_content']
        receiver = receiver.split(',')
        
        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()
            
        print receiver
        
        result = send_email(senders, receiver, content)
        
        if not result:
            return render_template('email.html', content="Email is sent")
        else:
            return render_template('email.html', content="Email is not sent")
        
    else:
        return render_template('email.html')
    
def send_email(senders, receiver, content):
    try:
        mail = Mail(app)
        msg = Message('Title', sender = senders, recipients = receiver)
        msg.body = content
        mail.send(msg)
    except Exception:
        pass 
    finally:
        pass

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    user = request.form['nm']   
    resp = make_response(render_template("readcookie.html"))
    resp.set_cookie('userID', user)   
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

# Unlike a cookie, session is stored on server side


@app.route('/result', methods=['POST', 'GET'])
def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template("result.html", result=result)
    return render_template('flash2.html')

@app.route('/<user>/<int:score>')
def index(user, score):
    dicts = {'phy':50, 'che':60, 'maths':70}
    return render_template('login.html', name=user, marks=score, result=dicts)

@app.route('/python')  # app.route(rule, options)
def hello_world():
    return 'Hello world'

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/<name>')  # app.route(rule, options)
def hello(name):
    if name is 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
    
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login_check', methods=['post', 'get'])
def login_check():
    return render_template('login_check.html')

@app.route('/login_inspect', methods=['post', 'get'])
def login_inspect():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success', name=user))
    
@app.route('/login', methods=['post', 'get'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

@app.route('/test', methods=['GET', 'POST'])
def flash_intro():
    error = None
    
    if request.method == 'POST':
        
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('test'))
        
    return render_template('test2.html', error=error)

@app.route('/')
def test():
    return render_template('test.html')

@app.route('/upload')
def upload_file():
    
    target_dir = os.path.normpath('C:/Users/David/git/Python_Project/Flask_Application/static/uploads')
    list = []
    for (path, dir, files) in os.walk(target_dir):      
        for fname in files:
            l_list = []
            fullfname ="/static/uploads/" + fname
            l_list.append(fullfname)
            l_list.append(fname)
            l_list.append(datetime.datetime.fromtimestamp(os.path.getatime(target_dir+'/'+fname)))
            list.append(l_list)
            print fullfname
    return render_template('upload.html', fileList=list)
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_run():
    if request.method == 'POST':
        f = request.files['file']
        print secure_filename(f.filename)
        if not os.path.isdir(app.config['UPLOAD_FOLDER']):
            os.makedirs('static/uploads')
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        else:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        
        target_dir = os.path.normpath('C:/Users/David/git/Python_Project/Flask_Application/static/uploads')
        list = []
        for (path, dir, files) in os.walk(target_dir):      
            for fname in files:
                l_list = []
                fullfname ="/static/uploads/" + fname
                l_list.append(fullfname)
                l_list.append(fname)
                l_list.append(datetime.datetime.fromtimestamp(os.path.getatime(target_dir+'/'+fname)))
                list.append(l_list)
                print fullfname
        return render_template('upload.html', fileList=list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # 127.0.0.1 / 5000 default

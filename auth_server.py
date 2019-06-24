from flask import Flask, request, Response, jsonify, views, render_template, url_for, redirect
import os
import datetime
import jwt as jwt
import random

import data_base_work as db


app = Flask(__name__)


def proove_auth():
    if 'auth_key' in request.headers:
        return True
    else:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='logon', port=port, methods="GET")


@app.route("/authenticate", methods=['GET'])
def authenticate():
    return render_template("login.html")



@app.route("/logon", methods=['GET'])
def logon():
        login = request.args.get('login')
        password = request.args.get('password')

        query = 'SELECT * FROM Users' \
                'WHERE Login=(%s) AND Password=(%s)'
        user = db.query_db(query, login, password)
    if user:

        token = create_jwt(login)
        resp = Response()
        resp.headers['auth_key'] = token

        ref = '/' #request.headers.get("Referer")
        if not ref:
            ref = '/'
        port = int(os.environ.get('PORT', 5000))
        app.run(host=ref, port=port)
    else:
        return 'Неверный логин или пароль!'


def create_jwt(login):
    payload = {
        'sub': login,
        # 'iat': datetime.date(),
        # 'exp': datetime.date() + datetime.timedelta(minutes=90)
    }
    salt = random.random() * 10000
    token = jwt.encode(payload, str(salt), algorithm='HS256')
    return token
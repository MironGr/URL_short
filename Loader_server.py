import json
import sqlite3 as lite
from flask import Flask, request, Response, jsonify, views, render_template, url_for, redirect
# import requests

import data_base_work as db
import methods as m

app = Flask(__name__)

#
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    return Response('Hello, World!')
#
# @app.route('/post-full-url/<path:full_url_address>')
# def short_url(full_url_address):
#     check_req = m.check_requests(full_url_address)
#
#
@app.route('/post-full-url/<username>')
def user_post(username):
    return 'User %s' % username
# def short_url(full_url_address):
#     return Response('Hello, World!22')


@app.route('/url-full/<path:url>')
def short_url(url):
    query_str = f'''INSERT INTO URL (URL_full, URL_short, Users_Id)
                        VALUES ('{url}', '5', 6);
                        '''
    db.query_save_db(query_str)
    return 'URL_full %s' % url

# @app.route('/url-short-make/<URLshort>')
# def URL_short(URLshort):
#     query_str = f'''INSERT INTO URL (URL_full, URL_short)
#                            VALUES ('{(URLshort)}', '2');
#             '''
#     db.query_save_db(query_str)
#     # with open("data_file.txt", "r") as read_file:
#     #     file_json = json.load(read_file)
#     # a = print(file_json)
#     return Response('Norm!')
#
# @app.route('/<path:full_url_address>')
# def get_full_url(full_url_address):
#     query_str = f'''INSERT INTO URL (URL_full, URL_short)
#                            VALUES ('{full_url_address}', '3');
#             '''
#     db.query_save_db(query_str)
#     return Response('URL is recorded')
#
# @app.route('/short/<path:short_url_address>')
# def connect_short_url(short_url_address):
#     conn = lite.connect('URL_short_server_1.db')
#     cursor = conn.cursor()
#     query_string = f'''select URL_full from URL
#                         where URL_short = {short_url_address}
#                     '''
#     cursor.execute(query_string)
#     data = cursor.fetchall()
#     # with open("data_file.txt", "r+") as write_file:
#     #     json.dump(data, write_file)
#     url = data(0)
#     print(url)
    # r = request.get(url)



# class UsersView(views.MethodView):
#     def get(self):
#         data = get_users()
#         return jsonify(data)
#
#     def post(self):
#         data = create_user(request.json)
#         return jsonify(data)
#
#
# app.add_url_rule('/users/', view_func=UsersView.as_view('users'))
import json
import sqlite3 as lite
from flask import Flask, request, Response, jsonify, views, render_template, url_for, redirect
import requests
# import request

import data_base_work as db
import methods as m
# import auth_server as auth


app = Flask(__name__)


#
# @app.route('/')
# def index():
#     return render_template('index.html')



@app.route('/')
def index():
    return Response('Hello, World!')

@app.route('/get_users')
def send_users():
    query = '''SELECT Login FROM Users;
            '''
    res = db.query_db(query)
    return jsonify(users=res)

@app.route('/short-full-url', methods=['POST'])
def short_url():
    # url_exist_db = m.check_short_url_address_in_database(full_url_address)
    # short_url = m.abbreviation_auto(full_url_address)
    # data =
    # with open(data, 'r') as f_:
    #     r = json.load(f_)
    return jsonify(full='is your short URL!')
    # if url_exist_db is False and short_url is True:
    #     return Response(short_url + ' is your short URL!')

# def short_url(full_url_address):
#     return Response('Hello, World!22')


# @app.route('/url-full/<path:url>')
# def short_url(url):
#     query_str = f'''INSERT INTO URL (URL_full, URL_short, Users_Id)
#                         VALUES ('{url}', '5', 6);
#                         '''
#     db.query_save_db(query_str)
#     return 'URL_full %s' % url

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
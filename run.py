from flask import Flask
from flask import json
from flask import request

from App import Api

app = Flask(__name__)


@app.route('/')
def hello_world():
    users = ['Linda', 'Marion5', 'Race8']
    return json.dumps(users), 404, [('Content-Type', 'application/json;charset=utf-8')]


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    return Api.login(username, password)


@app.route('/getUser')
def getUser():
    token = request.headers.get('token')
    return Api.getUser(token)


@app.route('/getArticleList')
def getArticleList():
    token = request.headers.get('token')
    return Api.getArticleList(token)


@app.route('/blog/<id>')
def get_blog(id):
    return Api.get_blog(id)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

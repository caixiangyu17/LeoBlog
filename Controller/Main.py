from flask import Flask
from flask import json
from flask import request

from App import Api

app = Flask(__name__)


@app.route('/')
def hello_world():
    users = ['Linda', 'Marion5', 'Race8']
    return json.dumps(users), 404, [('Content-Type', 'application/json;charset=utf-8')]


@app.route('/login', methods=['POST'])
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


@app.route('/getArticle/<articleId>')
def getArticle(articleId):
    return Api.getArticle(articleId)


@app.route('/postArticle', methods=['POST'])
def postArticle():
    data = {"token": request.headers.get('token'),
            "title": request.get_json()['title'],
            "titleEn": request.get_json()['titleEn'],
            "content": request.get_json()['content'],
            "contentEn": request.get_json()['contentEn'],
            }
    return Api.postArticle(data)


@app.route('/delArticle', methods=['DELETE'])
def delArticle():
    token = request.headers.get('token')
    articleId = request.get_json()['articleId']
    return Api.delArticle(token, articleId)


def getUser():
    token = request.headers.get('token')
    return Api.getUser(token)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

import json

from Test import TestManager


def test1():
    path = "/getArticleList"
    token = TestManager.login()
    resultMethod = TestManager.getByToken(path, {}, token)
    resultExpected = str(json.dumps({
        "code": 200,
        "data": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ],
        "message": "success"
    }))
    return [resultMethod, resultExpected]


def test2():
    path = "/getArticleList"
    token = TestManager.loginLeo()
    resultMethod = TestManager.getByToken(path, {}, token)
    resultExpected = str(json.dumps({
        "code": 200,
        "data": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ],
        "message": "success"
    }))
    return [resultMethod, resultExpected]

import json

from Test import TestManager


def test1():
    path = "/login"
    data = {
        "username": "test",
        "password": "test"
    }
    loginResult = json.loads(TestManager.post(path, data))
    token = loginResult['data']['token']
    path = "/delArticle"
    data = {
        "articleId": "4",
    }
    resultMethod = TestManager.delByToken(path, data, token)
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected, TestManager.TestManager.TYPE_REGEX]


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
    path = "/postArticle"
    data = {
        "title": "test1",
        "titleEn": "testEn",
        "content": "content",
        "contentEn": "contentEn",
    }
    resultMethod = TestManager.postByToken(path, data, token)
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected, TestManager.TestManager.TYPE_REGEX]

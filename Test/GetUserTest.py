import json

from App import ErrorResult
from Test import TestManager


def test1():
    path = "/login"
    data = {
        "username": "caixiangyu17",
        "password": "123456"
    }
    loginResult = json.loads(TestManager.post(path, data))
    token = loginResult['data']['token']
    path = "/getUser"
    resultMethod = TestManager.getByToken(path, {"a": "b"}, token)
    resultExpected = str(json.dumps({
        "code": 200,
        "data": {
            "id": 1,
            "name": "Leo",
            "username": "caixiangyu17",
            "description": "Trust no one, even your compiler!"
        },
        "message": "success"
    }))
    return [resultMethod, resultExpected, TestManager.TestManager.TYPE_EQUAL]


def test2():
    path = "/login"
    data = {
        "username": "admin",
        "password": "admin"
    }
    loginResult = json.loads(TestManager.post(path, data))
    token = loginResult['data']['token']
    path = "/getUser"
    resultMethod = TestManager.getByToken(path, {"a": "b"}, token)
    resultExpected = str(json.dumps({
        "code": 200,
        "data": {
            "id": 2,
            "name": "Admin",
            "username": "Admin",
            "description": "I am God."
        },
        "message": "success"
    }))
    return [resultMethod, resultExpected, TestManager.TestManager.TYPE_EQUAL]


def test3():
    path = "/getUser"
    resultMethod = TestManager.getByToken(path, {"a": "b"}, "sdfsjhldkfjklsdjflk")
    resultExpected = json.dumps(ErrorResult.TOKEN_ERROR)
    return [resultMethod, resultExpected, TestManager.TestManager.TYPE_EQUAL]

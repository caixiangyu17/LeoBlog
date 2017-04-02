from test import TestManager


def test1():
    path = "/login"
    data = {
        "username": "caixiangyu17",
        "password": "123456"
    }
    resultMethod = str(TestManager.post(path, data))
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected]


def test2():
    path = "/login"
    data = {
        "username": "admin",
        "password": "admin"
    }
    resultMethod = str(TestManager.post(path, data))
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected]


def test3():
    path = "/login"
    data = {
        "username": "admin",
        "password": "adminaaa"
    }
    resultMethod = str(TestManager.post(path, data))
    resultExpected = '"code" *: *401'
    return [resultMethod, resultExpected]


def testLogin4():
    path = "/login"
    data = {
        "username": "caixiangyu17",
        "password": "12345"
    }
    resultMethod = str(TestManager.post(path, data))
    resultExpected = '"code" *: *401'
    return [resultMethod, resultExpected]

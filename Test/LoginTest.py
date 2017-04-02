from Test import TestManager


def test1():
    path = "/login"
    data = {
        "username": "caixiangyu17",
        "password": "123456"
    }
    resultMethod = TestManager.post(path, data)
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected]


def test2():
    path = "/login"
    data = {
        "username": "admin",
        "password": "admin"
    }
    resultMethod = TestManager.post(path, data)
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected]


def test3():
    path = "/login"
    data = {
        "username": "admin",
        "password": "adminaaa"
    }
    resultMethod = TestManager.post(path, data)
    resultExpected = '"code" *: *401'
    return [resultMethod, resultExpected]


def testLogin4():
    path = "/login"
    data = {
        "username": "caixiangyu17",
        "password": "12345"
    }
    resultMethod = TestManager.post(path, data)
    resultExpected = '"code" *: *401'
    return [resultMethod, resultExpected]

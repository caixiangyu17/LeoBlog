from test import TestManager


def test1():
    path = "/"
    data = {
        "username": "caixiangyu17",
        "password": "123456"
    }
    resultMethod = str(TestManager.get(path, None))
    print(resultMethod)
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected]

test1()
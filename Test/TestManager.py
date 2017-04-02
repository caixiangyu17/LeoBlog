import http.client
import json
import unittest

from Test import GetArticleListTest
from Test import GetUserTest
from Test import LoginTest

url = "127.0.0.1"
port = 5000


def login():
    path = "/login"
    data = {
        "username": "test",
        "password": "test"
    }
    loginResult = json.loads(post(path, data))
    return loginResult['data']['token']


def loginLeo():
    path = "/login"
    data = {
        "username": "caixiangyu17",
        "password": "123456"
    }
    loginResult = json.loads(post(path, data))
    return loginResult['data']['token']


def post(path, data):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(url, port=port)
    conn.request("POST", path, json.dumps(data), headers)
    r = conn.getresponse()
    return str(r.read(), 'utf-8')


def get(path, data):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(url, port=port)
    conn.request("GET", path, json.dumps(data), headers)
    r = conn.getresponse()
    return str(r.read(), 'utf-8')


def getByToken(path, data, token):
    headers = {"Content-type": "application/json", "Accept": "text/plain", "token": token}
    conn = http.client.HTTPConnection(url, port=port)
    conn.request("GET", path, json.dumps(data), headers)
    r = conn.getresponse()
    return str(r.read(), 'utf-8')


class TestManager(unittest.TestCase):
    def testLogin1(self):
        testResult = LoginTest.test1()
        self.assertRegex(testResult[0], testResult[1])

    def testLogin2(self):
        testResult = LoginTest.test2()
        self.assertRegex(testResult[0], testResult[1])

    def testLogin3(self):
        testResult = LoginTest.test3()
        self.assertRegex(testResult[0], testResult[1])

    def testGetUser1(self):
        testResult = GetUserTest.test1()
        self.assertEqual(testResult[0], testResult[1])

    def testGetUser2(self):
        testResult = GetUserTest.test2()
        self.assertEqual(testResult[0], testResult[1])

    def testGetUser3(self):
        testResult = GetUserTest.test3()
        self.assertEqual(testResult[0], testResult[1])

    def testGetArticleList(self):
        testResult = GetArticleListTest.test1()
        self.assertEqual(testResult[0], testResult[1])


if __name__ == '__name__':
    unittest.main()

import http.client
import json
import unittest

from Test import DelArticleTest
from Test import GetArticleListTest
from Test import GetArticleTest
from Test import GetUserTest
from Test import LoginTest
from Test import PostArticleTest

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


def postByToken(path, data, token):
    headers = {"Content-type": "application/json", "Accept": "text/plain", "token": token}
    conn = http.client.HTTPConnection(url, port=port)
    conn.request("POST", path, json.dumps(data), headers)
    r = conn.getresponse()
    return str(r.read(), 'utf-8')


def delByToken(path, data, token):
    headers = {"Content-type": "application/json", "Accept": "text/plain", "token": token}
    conn = http.client.HTTPConnection(url, port=port)
    conn.request("DELETE", path, json.dumps(data), headers)
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
    TYPE_REGEX = 0
    TYPE_EQUAL = 1

    def testGetArticleList(self):
        testResult = GetArticleListTest.test1()
        self.check(testResult[0], testResult[1], 1)

    def check(self, resultMethod, resultExpected, testType):
        if testType == self.TYPE_EQUAL:
            self.assertEqual(resultMethod, resultExpected)
        elif testType == self.TYPE_REGEX:
            self.assertRegex(resultMethod, resultExpected)

    def testLogin1(self):
        testResult = LoginTest.test1()
        self.check(testResult[0], testResult[1], testResult[2])

    def testLogin2(self):
        testResult = LoginTest.test2()
        self.check(testResult[0], testResult[1], testResult[2])

    def testLogin3(self):
        testResult = LoginTest.test3()
        self.check(testResult[0], testResult[1], testResult[2])

    def testLogin4(self):
        testResult = LoginTest.test4()
        self.check(testResult[0], testResult[1], testResult[2])

    def testGetUser1(self):
        testResult = GetUserTest.test1()
        self.check(testResult[0], testResult[1], testResult[2])

    def testGetUser2(self):
        testResult = GetUserTest.test2()
        self.check(testResult[0], testResult[1], testResult[2])

    def testGetUser3(self):
        testResult = GetUserTest.test3()
        self.check(testResult[0], testResult[1], testResult[2])

    def testGetArticle(self):
        testResult = GetArticleTest.test1()
        self.check(testResult[0], testResult[1], testResult[2])

    def testPostArticle(self):
        testResult = PostArticleTest.test1()
        self.check(testResult[0], testResult[1], testResult[2])

    def testDelArticle(self):
        testResult = DelArticleTest.test1()
        self.check(testResult[0], testResult[1], testResult[2])


if __name__ == '__name__':
    unittest.main()

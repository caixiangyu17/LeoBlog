from Test import TestManager


def test1():
    path = "/getArticle/1"
    resultMethod = TestManager.get(path, {})
    resultExpected = '"code" *: *200'
    return [resultMethod, resultExpected, TestManager.TestManager.TYPE_REGEX]



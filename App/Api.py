import json
import uuid
from App import DatabaseManager
from App import ErrorResult


def createNetResult(code, data, message):
    return json.dumps({
        'code': code,
        'data': data,
        'message': message
    })



def hasResult(result):
    return len(result) > 0


def login(username, password):
    sqlResult = DatabaseManager.runSql(f'''
        select * from user
        where username ="{username}"
        and password = "{password}"
    ''')
    if hasResult(sqlResult):
        token = uuid.uuid4().hex
        DatabaseManager.runSql(f'''
        update user set token = "{token}"
        where username = "{username}"
        ''')
        code = 200
        data = {"token": token}
        message = "success"
        return createNetResult(code, data, message)
    else:
        return json.dumps(ErrorResult.USERNAME_ERROR)


def getUser(token):
    sqlResult = DatabaseManager.runSql(f"""
        select id, name, username, description
        from USER
        where token ="{token}"
    """)
    if hasResult(sqlResult):
        code = 200
        data = {
            "id": sqlResult[0][0],
            "name": sqlResult[0][1],
            "username": sqlResult[0][2],
            "description": sqlResult[0][3]
        }
        message = "success"
        return createNetResult(code, data, message)
    else:
        return json.dumps(ErrorResult.TOKEN_ERROR).encode("utf-8")


def getArticleList(token):
    userId = processToken(token)
    if userId == -1:
        return json.dumps(ErrorResult.TOKEN_ERROR).encode("utf-8")
    else:
        sqlResult = DatabaseManager.runSql(f"""
        select article.id
        from article
        where author_id = "{userId}"
    """)
    code = 200
    data = []
    if hasResult(sqlResult):
        for line in sqlResult:
            data.append({"id": line[0]})
    message = "success"
    return createNetResult(code, data, message)


def get_blog(id):
    return id


def processToken(token):
    sqlResult = DatabaseManager.runSql(f"""
        select id
        from user
        where token = "{token}"
    """)
    if hasResult(sqlResult):
        return sqlResult[0][0]
    else:
        return -1

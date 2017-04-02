import MySQLdb


def getDatabase():
    return MySQLdb.connect(host="localhost",  # your host, usually localhost
                           user="root",  # your username
                           passwd="Cxy759388",  # your password
                           db="blog")  # name of the data base


def runSql(sql):
    print("run sql: {}".format(sql))
    db = getDatabase()
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    db.commit()
    db.close()
    return result

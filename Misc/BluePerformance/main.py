import pymssql
import sqlinfo


def create_a_table(cursor):
    query = r"""
            CREATE TABLE AAA (id INT NOT NULL PRIMARY KEY ,
            numberOfCalls INT,
            totalTime FLOAT,
            timePerCall FLOAT,
            cumulativeTime FLOAT,
            commandID TEXT,
            runID TEXT);
            """
    cursor.execute(query)
    pass

def login():
    conn = pymssql.connect(sqlinfo.server, sqlinfo.user, sqlinfo.password, database=sqlinfo.database)
    cursor = conn.cursor()
    return cursor

cur = login()
create_a_table(cur)
pass

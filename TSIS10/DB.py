import psycopg2
#                CONNECT
def connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "sample",
        user = "postgre",
        password = "dbbase123")
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
connect()
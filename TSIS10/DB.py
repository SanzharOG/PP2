import psycopg2
#                CONNECT
def connect_table():
    conn = psycopg2.connect(
        host = "localhost",
        database = "sample",
        user = "postgre",
        password = "dbbase123")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE Info (
        username VARCHAR(255),
        age INTEGER
        joined DATE,
        hobby TEXT,
        password VARCHAR(255)

    );
    """)
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
    conn.commit()
#connect_table()

def insert():
    pass
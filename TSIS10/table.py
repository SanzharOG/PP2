import psycopg2
try:
    con = psycopg2.connect(database = "sample", user = "postgres",
                           password = "dbbase123", host = "localhost", port = "5432")    
    print('connected successfully')
except:
    print('no connect')
cur = con.cursor()
cur.execute('''
CREATE TABLE Info
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
EMAIL TEXT NOT NULL,
AGE INT NOT NULL,
HOBBY TEXT
)
''')
con.commit()
print("Table created Successfuly")
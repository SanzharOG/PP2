import psycopg2
try:
    con = psycopg2.connect(database = "sample", user = "postgres",
                           password = "dbbase123", host = "localhost", port = "5432")    
    print('connected successfully')
except:
    print('no connect')
cur = con.cursor()
cur.execute('SELECT ID , NAME , EMAIL, AGE, HOBBY from Info')
rows = cur.fetchall()
for data in rows:
    print("ID: " + str(data[0]))
    print("NAME: " + data[1])
    print("EMAIL: " + data[2])
    print("AGE: " + str(data[3]))
    print("HOBBY: " + data[4])

print("Data selected Successfully")
con.close()
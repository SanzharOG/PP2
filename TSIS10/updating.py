import psycopg2
try:
    con = psycopg2.connect(database = "sample", user = "postgres",
                           password = "dbbase123", host = "localhost", port = "5432")    
    print('connected successfully')
except:
    print('no connect')
cur = con.cursor()
cur.execute("UPDATE Info set EMAIL = 'zhassulanissayev@gmail.com' WHERE ID = 2665")
cur.execute("UPDATE Info set AGE = 18 WHERE hobby = 'dota'")
con.commit()
print("Data updated Successfully")
print('Total row affected ' + str(cur.rowcount))
con.close()
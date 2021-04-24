import psycopg2
try:
    con = psycopg2.connect(database = "sample", user = "postgres",
                           password = "dbbase123", host = "localhost", port = "5432")    
    print('connected successfully')
except:
    print('no connect')
cur = con.cursor()
cur.execute("DELETE FROM Info WHERE AGE = 17")
con.commit()
print("Data deleted Successfully")
con.close()
import psycopg2
try:
    con = psycopg2.connect(database = "sample", user = "postgres",
                           password = "dbbase123", host = "localhost", port = "5432")    
    print('connected successfully')
except:
    print('no connect')
cur = con.cursor()
cur.execute('''
INSERT INTO Info (ID,NAME,EMAIL,AGE,HOBBY) VALUES(12455,'Yerkin','e_baizhanov@kbtu.kz',17,'CS')
''')
con.commit()
print("Data inserted Successfully")
con.close()
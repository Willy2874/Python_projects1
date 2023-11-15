import sqlite3

connection =sqlite3.connectusers.db

cursor = connection.cursor()

#retrieving
users = cursor.execute ('''
    SELECT * FROM users
                        

''').fetchall()

for user in users:
    print (user[2])

    connection.commit()
    cursor.close()
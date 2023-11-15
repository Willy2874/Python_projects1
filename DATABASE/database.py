import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

#transaction
cursor.execute('''
    CREATE TABLE users(
               first_name TEXT,
               last_name TEXT
               age INTEGER
    )
''')

#transact (insert users)
cursor.execute('''
INSERT INTO users VALUES (?,?,?)
               ('Dennis', 'Mbaya', '20')
               ('Dennis', 'Mbaya', '20')

''',)


#save transactions
connection.commit()

cursor.close()
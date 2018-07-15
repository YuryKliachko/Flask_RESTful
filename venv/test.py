import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

add_user = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(add_user, (1, 'yury', '123123'))

users = [
    (2, "john", "323232"),
    (3, "david", "123456")
]

cursor.executemany(add_user, users)

retrieve_user = "SELECT * FROM users"
for row in cursor.execute(retrieve_user):
    print(row)

connection.commit()
connection.close()
import sqlite3

connection = sqlite3.connect("gpr.db")
cursor = connection.cursor()

query = "SELECT * FROM User;"
cursor.execute(query)

result = cursor.fetchall()
print(result)

connection.commit()
connection.close()
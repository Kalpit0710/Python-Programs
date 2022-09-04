import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "1234"
)

cursor = mydb.cursor()
cursor.execute("SHOW DATABASE")

for x in cursor:
print(x)
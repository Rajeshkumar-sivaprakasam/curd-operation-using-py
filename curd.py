

import mysql.connector as mysql

db_connection = mysql.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "db_set"
	)
db_cursor = db_connection.cursor()
print("Successfully db_connection established & Cursor created!")


"""def createTable():
	sql = "create table user(id INT, name VARCHAR(255))"
	db_cursor.execute(sql)
	return "Table created Successfully"

	"""

def addRow():
	sql = "insert into user(id,name) values(%s,%s)"
	values = (12,"Sathish")
	db_cursor.execute(sql,values)
	db_connection.commit()
	return "%s Added Successfully" %(db_cursor.rowcount)

def deleteRow():
	sql = "delete from user where id =12 "
	db_cursor.execute(sql)
	db_connection.commit()
	return "%s deleted Successfully" %(db_cursor.rowcount)

def updateRow():
	sql = "update user set id =100 where name ='rajesh' "
	db_cursor.execute(sql)
	db_connection.commit()
	return "%s updated Successfully" %(db_cursor.rowcount)

def toView():
	sql = "select * from user"
	db_cursor.execute(sql)
	list_row = db_cursor.fetchall()
	for i in list_row:
		print(i)

print("1.addRow \n2.delete \n3.update \n4.view")
option = int(input())

if option == 1:
	#print(createTable())
	print(addRow())

elif option == 2:
	print(deleteRow())

elif option == 3:
	print(updateRow())

elif option == 4:
	toView()	
else:
	print("select a valid one")


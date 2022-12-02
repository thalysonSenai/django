""" from xml.etree.ElementInclude import include
import mysql.connector
from mysql.connector import errorcode

try:
	cnx = mysql.connector.connect(user='root', password='Senai2019,', port='3306', database='world')
	print ("success")
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cnx.close()

cnx.reconnect()
cursor = cnx.cursor() 
text_cidade = "hogwarts"
cidade = "Curitiba"
cursor.execute('select name from city where id = 212')
if cidade in cursor:
	print(cursor)
	print("essa cidade do brasil")
 """

u = {}
u["nome"] = "thalyson"
print(u['nome'])
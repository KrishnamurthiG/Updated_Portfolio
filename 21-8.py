#importing MySQL API
import MySQLdb

#establishing database connection
dbcon = MySQLdb.connect('localhost','root','root','python2_db')

#cursor object creation
cursorobj = dbcon.cursor()

#executing SQL Queries using execute().....
cursorobj.execute("select * from student")

#fetching a single row using fetchone().....
data = cursorobj.fetchone()

print(data)

#closing the connection
dbcon.close()
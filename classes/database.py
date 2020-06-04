# *****************************************************************************************
class Database:
	connected = True
	error = ''
	tables = []
	db_conn = ''
	cursor = ''

	# ***************************************************
	def __init__(self):
		import databaseconfig
		import mysql.connector
		from mysql.connector import errorcode


		try:
			Database.db_conn = mysql.connector.connect(user=databaseconfig.dbinfo['user'], password=databaseconfig.dbinfo['password'], host=databaseconfig.dbinfo['host'], database=databaseconfig.dbinfo['database'], port=databaseconfig.dbinfo['port'])
		except mysql.connector.Error as err:
			Database.connected = False
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				Database.error = "Database Error: Something is wrong with your user name or password"
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				Database.error = "Database Error: Database does not exist"
			else:
				Database.error = err

		if Database.connected is True:
			#self.db_conn.cursor(prepared=True, dictionary=True) will cause an error, there's a bug that doesnt allow prepared and the use of column name returns to be used at the same time
			Database.cursor = Database.db_conn.cursor(dictionary=True)
			self.get_tables()
	# ***************************************************


	# ***************************************************
	def get_tables(self):
		sql = ("show tables")
		Database.cursor.execute(sql) 
		results = Database.cursor.fetchall()

		for row in results:
			Database.tables.append(row['Tables_in_dms'])
	# ***************************************************


	# ***************************************************
	def close(self):
		Database.db_conn.close()
		Database.connected = False
	# ***************************************************

# *****************************************************************************************

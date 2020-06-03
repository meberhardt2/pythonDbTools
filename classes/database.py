# *****************************************************************************************
class Database:
	connected = True
	error = ''

	# ***************************************************
	def __init__(self):
		import mysql.connector
		from mysql.connector import errorcode
		import databaseconfig


		self.db_conn = ''
		self.cursor = ''
		self.tables = []


		try:
			self.db_conn = mysql.connector.connect(user=databaseconfig.dbinfo['user'], password=databaseconfig.dbinfo['password'], host=databaseconfig.dbinfo['host'], database=databaseconfig.dbinfo['database'], port=databaseconfig.dbinfo['port'])
		except mysql.connector.Error as err:
			Database.connected = False
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				Database.error = "Something is wrong with your user name or password"
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				Database.error = "Database does not exist"
			else:
				Database.error = err

		if Database.connected is True:
			self.cursor = self.db_conn.cursor(prepared=True)
			self.get_tables()
	# ***************************************************


	# ***************************************************
	def get_tables(self):
		sql = ("show tables")
		self.cursor.execute(sql) 
		results = self.cursor.fetchall()

		for row in results:
			self.tables.append(row[0])
	# ***************************************************


	# ***************************************************
	def close(self):
		self.db_conn.close()
		Database.connected = False
	# ***************************************************

# *****************************************************************************************

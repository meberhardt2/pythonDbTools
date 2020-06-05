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

		available_dbs = []
		for item in databaseconfig.databases:
			available_dbs.append(item)

		print('Available databases:')
		counter = 0
		for item in available_dbs:
			print(str(counter)+' = '+item)
		print()
		
		looping = True
		while looping:
			try:
				config_number = int(input())
			except:
				config_number = 'bad'
				print('invalid entry. try again.')			
			if isinstance(config_number, int) and config_number < len(available_dbs):
				looping = False
		
		config = available_dbs[config_number]

		try:
			Database.db_conn = mysql.connector.connect(user=databaseconfig.databases[config]['user'], password=databaseconfig.databases[config]['password'], host=databaseconfig.databases[config]['host'], database=databaseconfig.databases[config]['database'], port=databaseconfig.databases[config]['port'])
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

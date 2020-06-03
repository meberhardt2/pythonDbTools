# *****************************************************************************************
class Database:

	# ***************************************************
	def __init__(self):
		import mysql.connector
		import databaseconfig

		self.db_conn = mysql.connector.connect(user=databaseconfig.dbinfo['user'], password=databaseconfig.dbinfo['password'], host=databaseconfig.dbinfo['host'], database=databaseconfig.dbinfo['database'], port=databaseconfig.dbinfo['port'])

# *****************************************************************************************

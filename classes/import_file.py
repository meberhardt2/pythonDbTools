# *****************************************************************************************
class ImportFile:
	running = ''

	# ***************************************************
	def __init__(self):
		self.keypress = ''
		self.filename = ''
		self.import_table = ''
		self.database = ''
		self.file_columns = []
	# ***************************************************


	# ***********************************
	def scan_dir(self):
		from os import listdir
		from os.path import isfile, join
		from common.utilities import menu_builder
		
		file_system_errors = False

		menu_config = {
			'config': {
				'title': 'Select File',
				'subtitle': ''
			},
			'menu_entries':  []
		}

		try:
			all_files = [f for f in listdir('process_files/') if isfile(join('process_files/', f))]
		except:
			file_system_errors = True


		if file_system_errors is True:
			menu_config['config']['subtitle'] = 'missing the folder process_files in this directory'


		if file_system_errors is False:
			counter = 0
			for item in all_files:
				menu_config['menu_entries'].append(
					{
						'display': str(counter)+" = "+item,
						'key': counter,
						'run_function': ''
					}
				)
				counter += 1


		menu_config['menu_entries'].append(
			{
				'display': "c = cancel",
				'key': 'c',
				'run_function': self.menu
			}
		)


		self.keypress = menu_builder(menu_config)


		if self.keypress == 'c':
			#nothing has to be done here, it will return to the loop in main
			pass
		else:
			if file_system_errors is False:
				bad_keypress = False
				#case str to int. if they typed in a letter, then dont go forward
				try:
					index = int(self.keypress)
				except:
					bad_keypress = True
					self.scan_dir()
				
				if bad_keypress is False:
					if index >= len(all_files):
						self.scan_dir()
					else:
						self.filename = all_files[index]
						self.prep()
	# ***********************************


	# ***********************************
	def prep(self):
		from common.utilities import menu_builder
		from classes.database import Database			# pylint: disable=no-name-in-module

		menu_config = {
			'config': {
				'title': 'Import File',
				'subtitle': ''
			},
			'menu_entries':  []
		}

		self.keypress = menu_builder(menu_config)

		self.database = Database()
		if self.database.error != '':
			print()
			print(self.database.error)
			print('Press enter to go back to the main menu')
			input()
			ImportFile.running = False
		else:
			while True:
				proceed = self.check_table()
				if proceed is True:
					break
				else:
					print("Table doesn't exist. Try again")

			if self.check_columns() is False:
				print("The above columns don't exist")
				print('Press enter to go back to the main menu')
				input()
				ImportFile.running = False
				self.database.close()
			else:
				self.import_file()
	# ***********************************


	# ***********************************
	def import_file(self):
		cursor = self.database.db_conn.cursor(dictionary=True)

		columns = ",".join(self.file_columns)
		sql = "LOAD DATA LOCAL INFILE 'process_files/"+self.filename+"' INTO TABLE "+self.import_table+" FIELDS TERMINATED BY '\\t' LINES TERMINATED BY '\\n' IGNORE 1 LINES ("+columns+")"
		cursor.execute(sql)
		input('done. press return to go back to the main menu') 
		ImportFile.running = False
		self.database.close()
	# ***********************************


	# ***********************************
	def check_table(self):
		self.import_table = input('What is the import table name: ')

		if self.import_table not in self.database.tables:
			return False
		else:
			return True
	# ***********************************


	# ***********************************
	def check_columns(self):
		cursor = self.database.db_conn.cursor(dictionary=True)
		first_line = ''
		table_columns = []
		proceed = True

		with open('process_files/'+self.filename) as f:
			first_line = f.readline()
		
		self.file_columns = first_line.split("\t")

		if len(self.file_columns) < 2:
			proceed = False
			print('Check file format')

		for i in range(len(self.file_columns)):
			self.file_columns[i] = self.file_columns[i].replace("\n",'')

		sql = "describe "+self.import_table
		cursor.execute(sql) 
		results = cursor.fetchall()

		for row in results:
			if row['Field'] != 'id':
				table_columns.append(row['Field'])

		for item in self.file_columns:
			if item not in table_columns:
				print(item)
				proceed = False

		#sql = "select * from temp_table where firstname = %s"
		#cursor.execute(insert_query, (string1, string2), multi=True)
		#the trailing comma is needed for single
		#cursor.execute(sql, (test,)) 
		#results = cursor.fetchall()

		return proceed
	# ***********************************


	# ***********************************
	def to_main_menu(self):
		#set running to false, the while loop in main will exit and return back to the main loop in main
		ImportFile.running = False
	# ***********************************


	# ***********************************
	def menu(self):
		from common.utilities import menu_builder

		menu_config = {
			'config': {
				'title': 'File Importer',
				'subtitle': ''
			},
			'menu_entries':  [
				{
					'display': 's = scan process_files',
					'key': 's',
					'run_function': self.scan_dir
				},
				{
					'display': 'm = main menu',
					'key': 'm',
					'run_function': self.to_main_menu
				}
			]
		}


		self.keypress = menu_builder(menu_config)


		for item in menu_config['menu_entries']:
			if item['key'] == self.keypress:
				item['run_function']()
				break
	# ***********************************


	# ***********************************
	def main(self):
		#import ../../databaseconfig as dbinfo
		#connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])
		ImportFile.running = True

		while ImportFile.running:
			self.menu()
	# ***********************************


# *****************************************************************************************

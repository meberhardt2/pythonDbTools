# *****************************************************************************************
class ImportFile:
	running = ''

	# ***************************************************
	def __init__(self):
		self.keypress = ''
		self.filename = ''
		self.import_table = ''
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
						'display': "{} = {}".format(counter, item),
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
						self.import_file()
	# ***********************************


	# ***********************************
	def import_file(self):
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

		print('What is the import table name: ')
		self.import_table = input()

		#check if the table exists
		Database()
		if Database.error != '':
			print()
			print(Database.error)
			print('Press enter to go back to the main menu')
			input()
			ImportFile.running = False

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
					'display': 'm = main menu',
					'key': 'm',
					'run_function': self.to_main_menu
				},
				{
					'display': 's = scan process_files',
					'key': 's',
					'run_function': self.scan_dir
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

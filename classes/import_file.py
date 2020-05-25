# *****************************************************************************************
class ImportFile:
	running = ''

	# ***********************************
	def __init__(self, curses, screen):
		self.curses = curses
		self.screen = screen

		self.keypress = ''
		self.ycoord = 0
		self.xcoord = 0
		self.screen_height = curses.LINES
		self.screen_width = curses.COLS

		self.filename = ''
	# ***********************************


	# ***********************************
	def scanDir(self):
		from os import listdir
		from os.path import isfile, join
		from common.utilities import MenuBuilder
		
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
			counter = 1
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


		self.keypress = MenuBuilder(self.curses, self.screen, menu_config)


		if self.keypress == 'c':
			self.menu()
		else:
			self.filename = all_files[self.keypress]
	# ***********************************


	# ***********************************
	def to_main_menu(self):
		#set running to false, the while loop in main will exit and return back to the main loop in main
		ImportFile.running = False
	# ***********************************


	# ***********************************
	def menu(self):
		from common.utilities import MenuBuilder

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
					'run_function': self.scanDir
				}
			]
		}


		self.keypress = MenuBuilder(self.curses, self.screen, menu_config)


		for item in menu_config['menu_entries']:
			if item['key'] == self.keypress:
				item['run_function']()
				break

	# ***********************************


	# ***********************************
	def main(self):
		ImportFile.running = True

		while ImportFile.running:
			self.menu()
	# ***********************************


# *****************************************************************************************

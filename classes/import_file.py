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

		menu_config = []

		try:
			all_files = [f for f in listdir('process_files/') if isfile(join('process_files/', f))]
		except:
			file_system_errors = True

		if file_system_errors is True:
			menu_config = {
				'config': {
					'title': 'Select File',
					'subtitle': 'missing the folder process_files in this directory'
				},
				'menu_entries':  [
					{
						'display': 'c = cancel',
						'key': 'i',
						'function': self.menu()
					}
				]
			}

		if file_system_errors is False:
			menu_config = {
				'config': {
					'title': 'Select File',
					'subtitle': ''
				},
				'menu_entries':  []
			}

			counter = 1
			for item in all_files:
				menu_config['menu_entries'].append(
					{
						'display': "{} = {}".format(counter, item),
						'key': counter,
						'function': ''
					}
				)
				counter += 1

			menu_config['menu_entries'].append(
				{
					'display': "c = cancel",
					'key': 'c',
					'function': ''
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
		menu_entries = []
		height_minus_menu = 0
		width_minus_menu = 0

		menu_entries = [{
			'display': 'm = main menu',
			'key': 'm',
			'function': self.to_main_menu
		},
		{
			'display': 's = scan process_files',
			'key': 's',
			'function': self.scanDir
		}]

		height_minus_menu = self.screen_height - len(menu_entries)
		self.ycoord = round(height_minus_menu / 2)

		width_minus_menu = self.screen_width - 10
		self.xcoord = round(width_minus_menu / 2)

		self.screen.clear()
		self.screen.addstr(self.ycoord,self.xcoord - 2, 'File Importer')
		self.ycoord += 1
		self.screen.addstr(self.ycoord,self.xcoord - 6, '-----------------------')
		self.ycoord += 1

		for item in menu_entries:
			self.screen.addstr(self.ycoord,self.xcoord, item['display'])
			self.ycoord += 1
		self.screen.refresh()

		self.keypress = self.screen.getkey()

		for item in menu_entries:
			if item['key'] == self.keypress:
				item['function']()
				break

	# ***********************************


	# ***********************************
	def main(self):
		ImportFile.running = True

		while ImportFile.running:
			self.menu()
	# ***********************************

# *****************************************************************************************

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
	def to_main_menu(self):
		#set running to false, the while loop in main will exit and return back to the main loop in main
		ImportFile.running = False
	# ***********************************


	# ***********************************
	def scanDir(self):
		from os import listdir
		from os.path import isfile, join

		height_minus_menu = 0
		width_minus_menu = 0

		all_files = [f for f in listdir('../process_files/') if isfile(join('../process_files/', f))]

		height_minus_menu = self.screen_height - len(all_files)
		self.ycoord = round(height_minus_menu / 2)

		width_minus_menu = self.screen_width - 10
		self.xcoord = round(width_minus_menu / 2)

		self.screen.clear()
		self.screen.addstr(self.ycoord,self.xcoord - 2, 'Select File')
		self.ycoord += 1
		self.screen.addstr(self.ycoord,self.xcoord - 6, '-----------------------')
		self.ycoord += 1

		counter = 1
		for item in all_files:
			self.screen.addstr(self.ycoord,self.xcoord, "{} = {}".format(counter, item))
			self.ycoord += 1
			counter += 1
		self.screen.refresh()

		self.screen.addstr(self.ycoord,self.xcoord, "c = cancel")
		self.ycoord += 1

		self.keypress = self.screen.getkey()

		if self.keypress == 'c':
			self.menu()
	# ***********************************


	# ***********************************
	def main(self):
		ImportFile.running = True

		while ImportFile.running:
			self.menu()
	# ***********************************

# *****************************************************************************************

# *****************************************************************************************
class ImportFile:
	running = True

	# ***********************************
	def __init__(self, curses, screen):
		self.curses = curses
		self.screen = screen

		self.main()
	# ***********************************


	# ***********************************
	def menu(self):
		keypress = ''
		ycoord = 0
		xcoord = 0
		menu_entries = []
		screen_height = self.curses.LINES
		screen_width = self.curses.COLS

		menu_entries = [{
			'display': 'm = main menu',
			'key': 'm',
			'function': self.to_main_menu
		}]

		height_minus_menu = screen_height - len(menu_entries)
		ycoord = round(height_minus_menu / 2)

		width_minus_menu = screen_width - 10
		xcoord = round(width_minus_menu / 2)

		self.screen.clear()
		self.screen.addstr(ycoord,xcoord - 2, 'File Importer')
		ycoord += 1
		self.screen.addstr(ycoord,xcoord - 6, '-----------------------')
		ycoord += 1

		for item in menu_entries:
			self.screen.addstr(ycoord,xcoord, item['display'])
			ycoord += 1
		self.screen.refresh()

		keypress = self.screen.getkey()

		for item in menu_entries:
			if item['key'] == keypress:
				item['function']()

	# ***********************************


	# ***********************************
	def to_main_menu(self):
		#set running to false, the while loop in main will exit and return back to the main loop in main
		ImportFile.running = False
	# ***********************************


	# ***********************************
	def main(self):
		while ImportFile.running:
			self.menu()
	# ***********************************

# *****************************************************************************************

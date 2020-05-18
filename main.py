import curses	# pylint: disable=unused-wildcard-import
from classes.import_file import ImportFile # pylint: disable=no-name-in-module

# ***********************************
running = True
screen = ''
# ***********************************


# ***********************************
def mainMenu():
	global screen

	keypress = ''
	ycoord = 0
	xcoord = 0
	menu_entries = []
	screen_height = curses.LINES					# pylint: disable=no-member
	screen_width = curses.COLS						# pylint: disable=no-member

	import_file = ImportFile(curses, screen)

	menu_entries = [{
		'display': 'i = import',
		'key': 'i',
		'function': import_file.main
	},
	{
		'display': 'q = quit',
		'key': 'q',
		'function': quit
	}]

	height_minus_menu = screen_height - len(menu_entries)
	ycoord = round(height_minus_menu / 2)

	width_minus_menu = screen_width - 10
	xcoord = round(width_minus_menu / 2)

	screen.clear()
	screen.addstr(ycoord,xcoord - 2, 'Db Tools v 0.1')
	ycoord += 1
	screen.addstr(ycoord,xcoord - 6, '-----------------------')
	ycoord += 1

	for item in menu_entries:
		screen.addstr(ycoord,xcoord, item['display'])
		ycoord += 1
	screen.refresh()

	keypress = screen.getkey()

	for item in menu_entries:
		if item['key'] == keypress:
			item['function']()
			keypress = ''
			break
# ***********************************


# ***********************************
def quit():
	global screen, running

	running = False

	curses.nocbreak()					# pylint: disable=no-member
	screen.keypad(False)
	curses.echo()						# pylint: disable=no-member
	curses.endwin()						# pylint: disable=no-member
# ***********************************


# *****************************************************************************************
def main():
	global screen

	screen = curses.initscr()
	curses.noecho()							# pylint: disable=no-member
	screen.keypad(True)
	curses.curs_set(False)					# pylint: disable=no-member
	#curs_set(True)					# pylint: disable=undefined-variable

	while running:
		mainMenu()

	#refresh() or window.refresh()? screen.refresh()?
	#terminate cursors
	#stdscr.nocbreak()
	#stdscr.keypad(False)
	#stdscr.echo()
	#stdscr.endwin()
# *****************************************************************************************


# *****************************************************************************************
if __name__ == '__main__':
	main()
# *****************************************************************************************

import curses	# pylint: disable=unused-wildcard-import
from classes.import_file import ImportFile # pylint: disable=no-name-in-module
from common.utilities import MenuBuilder

# ***********************************
running = True
screen = ''
# ***********************************


# ***********************************
def mainMenu():
	global screen

	keypress = ''
	menu_config = []

	import_file = ImportFile(curses, screen)

	menu_config = {
		'config': {
			'title': 'Db Tools v 0.1',
			'subtitle': ''
		},
		'menu_entries':  [
			{
				'display': 'i = import',
				'key': 'i',
				'function': import_file.main
			},
			{
				'display': 'q = quit',
				'key': 'q',
				'function': quit
			}
		]
	}

	keypress = MenuBuilder(curses, screen, menu_config)

	for item in menu_config['menu_entries']:
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


# ***********************************
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
# ***********************************


# ***********************************
if __name__ == '__main__':
	main()
# ***********************************

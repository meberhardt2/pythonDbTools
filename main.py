from classes.import_file import ImportFile # pylint: disable=no-name-in-module
from common.utilities import MenuBuilder

# ***********************************
running = True
# ***********************************


# ***********************************
def mainMenu():
	keypress = ''
	menu_config = []

	import_file = ImportFile()

	menu_config = {
		'config': {
			'title': 'Db Tools v 0.1',
			'subtitle': ''
		},
		'menu_entries':  [
			{
				'display': 'i = import',
				'key': 'i',
				'run_function': import_file.main
			},
			{
				'display': 'q = quit',
				'key': 'q',
				'run_function': quit
			}
		]
	}

	keypress = MenuBuilder(menu_config)

	for item in menu_config['menu_entries']:
		if item['key'] == keypress:
			item['run_function']()
			keypress = ''
			break
# ***********************************


# ***********************************
def quit():
	global running

	running = False
# ***********************************


# ***********************************
def main():
	while running:
		mainMenu()
# ***********************************


# ***********************************
if __name__ == '__main__':
	main()
# ***********************************

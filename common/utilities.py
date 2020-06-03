# ***********************************
def clear_screen():
	import os
	import platform

	platform = platform.system()

	if platform == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
# ***********************************


# ***********************************
def menu_builder(menu_config):
	keypress = ''

	clear_screen()

	print(menu_config['config']['title'])
	print('-----------------------')

	if(menu_config['config']['subtitle'] != ''):
		print(menu_config['config']['subtitle'])

	for item in menu_config['menu_entries']:
		print(item['display'])

	print('')

	if len(menu_config['menu_entries']) > 0:
		keypress = input()
	
	return keypress
# ***********************************

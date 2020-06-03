
# ***********************************
def MenuBuilder(menu_config):
	import os
	import platform

	keypress = ''
	platform = platform.system()

	if platform == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

	print(menu_config['config']['title'])
	print('-----------------------')

	if(menu_config['config']['subtitle'] != ''):
		print(menu_config['config']['subtitle'])

	for item in menu_config['menu_entries']:
		print(item['display'])

	if len(menu_config['menu_entries']) > 0:
		keypress = input()

	return keypress
# ***********************************

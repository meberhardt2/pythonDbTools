
# ***********************************
def MenuBuilder(curses, screen, menu_config):
	ycoord = 0
	xcoord = 0
	screen_height = curses.LINES					# pylint: disable=no-member
	screen_width = curses.COLS						# pylint: disable=no-member

	height_minus_menu = screen_height - len(menu_config['menu_entries'])
	ycoord = round(height_minus_menu / 2)

	width_minus_menu = screen_width - 10
	xcoord = round(width_minus_menu / 2)

	screen.clear()
	screen.addstr(ycoord,xcoord - 2, menu_config['config']['title'])
	ycoord += 1
	screen.addstr(ycoord,xcoord - 6, '-----------------------')
	ycoord += 1

	if(menu_config['config']['subtitle'] != ''):
		screen.addstr(ycoord,xcoord - 2, menu_config['config']['subtitle'])
		ycoord += 1

	for item in menu_config['menu_entries']:
		screen.addstr(ycoord,xcoord, item['display'])
		ycoord += 1
	screen.refresh()

	keypress = screen.getkey()

	return keypress
# ***********************************

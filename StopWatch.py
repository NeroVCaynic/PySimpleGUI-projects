import PySimpleGUI as sg

def Watch(theme):
	sg.theme(theme)
	box = [
		[sg.Button('T', size=(2,1), key='Theme')],
		[sg.Text(0, key='timer', expand_x=True, justification='center', font='cursive 45', pad=(30,30))],
		[sg.Button('Start', size=(10,3), pad=(4,4), key='start'), sg.Button('Reset', size=(10,3), pad=(4,4), key='reset')]
	]
	return sg.Window('Stop Watch', box)

window = Watch('LightGrey')
curColor = 'LightGrey'

while True:
	events, values = window.read()

	if events == 'Theme':
		if curColor == 'LightGrey':
			window.close()
			curColor = 'Dark'
			window = Watch('Dark')
		else:
			if curColor == 'Dark':
				window.close()
				curColor = 'LightGrey'
				window = Watch('LightGrey')				

	if events == 'start':
		window['timer'].update()

	if events == 'reset':
		window['timer'].update(0)

	if events == sg.WIN_CLOSED:
		break


window.close()
import PySimpleGUI as sg
from time import time

def Watch(theme):
	sg.theme(theme)
	themeMenu = ['theme',['Black','Dark']]
	box = [
		[sg.Push(), sg.Button('X', key='exit', size=(1,0), pad=(0,0), button_color=('#FFFFFF','#FF0000'), border_width=0)],
		[sg.VPush()],
		[sg.Text(0, key='timer', expand_x=True, justification='center', font='Young 45', pad=(10,10))],
		[sg.Button('Start', size=(10,3), pad=(4,4), key='startStop', button_color=('#FFFFFF','#FF0000'), border_width=0), 
		sg.Button('Reset', size=(10,3), pad=(4,4), key='reset', button_color=('#FFFFFF','#FF0000'), border_width=0)],
		[sg.VPush()]
	]
	return sg.Window('Stop Watch', box, size=(300,300), no_titlebar=True, element_justification='center', right_click_menu=themeMenu)

window = Watch('Black')
themeMenu = ['theme',['Black','Dark']]
startTime = 0
active = False

while True:
	events, values = window.read(timeout=10)

	if events in themeMenu[1]:
		window.close()
		window = Watch(events)
		continue

	if events == 'startStop':
		if active:
			active = False
			window['startStop'].update('Start')
		else:
			startTime = time()
			active = True
			window['startStop'].update('Stop')

	if active:
		elapsedTime = round(time() - startTime, 1)
		window['timer'].update(elapsedTime)

	if events == 'reset':
		startTime = 0
		window['timer'].update(0)
		active = False

	if events in (sg.WIN_CLOSED, 'exit'):
		break


window.close()
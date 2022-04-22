import PySimpleGUI as psg

def screen(theme):
	psg.theme(theme)
	outputFrame = [[psg.Text('Output:', key='output',pad=(5,8), font=['10'])]]
	convMethod = ['days to hrs','hrs to mins','Min to secs']
	app = [
		[psg.Input(key='inputBar', pad=(5,5), font=['10']), psg.Spin(convMethod, key='convWheel', pad=(5,5), font=['20'], size=(10,10))],
		[psg.Button("Submit", key='submit', expand_x=True, pad=(5,5), size=(6,3)), psg.Button("Exit", key='exit', pad=(5,5), size=(6,3))],
		[psg.Frame('',outputFrame, expand_x=True, pad=(5,5))]
	]
	return psg.Window("Convertor", app, right_click_menu=themeMenu)


themeMenu = ['theme',['BlueMono','Dark','DarkBrown3']]

window = screen('BlueMono')

while True:
	event, values = window.read()

	if event in themeMenu[1]:
		window.close()
		window = screen(event)
		continue

	if event == 'submit':
		value = values['inputBar']
		if value.isnumeric():
			if values['convWheel'] == 'Min to secs':
				window['output'].update(f'Output: {value} mins is {round(float(value)*60,2)} secs')
				continue

			elif values['convWheel'] == 'hrs to mins':
				window['output'].update(f'Output: {value} hrs is {round(float(value)*60,2)} mins')
				continue

			elif values['convWheel'] == 'days to hrs':
				window['output'].update(f'Output: {value} days is {round(float(value)*24,2)} hrs')
				continue
		else:
			psg.Popup('Wrong Input', keep_on_top=True, font=['15'])
			continue

	if event == psg.WIN_CLOSED or 'exit':
		break

window.close()
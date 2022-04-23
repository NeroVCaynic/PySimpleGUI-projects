import PySimpleGUI as sg

def calcScreen(theme):
	sg.theme(theme)
	sizeTup = (8,4)
	layout = [
		[sg.Text('', key='outputBox', justification='right', expand_x=True, font='Cursive 30', pad=(10,10), right_click_menu=themeMenu)],
		[sg.Button('Enter', key='enter', size=(sizeTup), expand_x=True), sg.Button('Clear', key='clear', size=(sizeTup), expand_x=True)],
		[sg.Button('1', key='1', size=(sizeTup)), sg.Button('2', key='2', size=(sizeTup)), sg.Button('3', key='3', size=(sizeTup)), sg.Button('X', key='*', size=(sizeTup))],
		[sg.Button('4', key='4', size=(sizeTup)), sg.Button('5', key='5', size=(sizeTup)), sg.Button('6', key='6', size=(sizeTup)), sg.Button('/', key='/', size=(sizeTup))],
		[sg.Button('7', key='7', size=(sizeTup)), sg.Button('8', key='8', size=(sizeTup)), sg.Button('9', key='9', size=(sizeTup)), sg.Button('-', key='-', size=(sizeTup))],
		[sg.Button('0', key='0', size=(sizeTup), expand_x=True), sg.Button('.', key='.', size=(sizeTup)), sg.Button('+', key='+', size=(sizeTup))]
	]
	return sg.Window('Calculator', layout)

outputL = []
outputR = []
operator = ''
themeMenu = ['theme',['BlueMono','Dark','DarkBrown3', 'LightGrey', 'Black', 'DarkRed1']]
window = calcScreen('LightGrey')

while True:
	events, values = window.read()

	if events in themeMenu[1]:
		window.close()
		window = calcScreen(events)
		continue

	if events in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
		if operator == '':
			outputL.append(events)
			window['outputBox'].update(''.join(outputL))
		else:
			outputR.append(events)
			window['outputBox'].update(''.join(outputR))

	if events in ['*','+','-','/']:
		if len(outputR) <= 0 and len(outputL) > 0:
			operator = events
			window['outputBox'].update(str(operator))
		else:
			pass

	if events == 'clear':
		outputL = []
		outputR = []
		operator = ''
		window['outputBox'].update('')

	if events == 'enter':
		L = ''.join(outputL)
		R = ''.join(outputR)
		output =  L + " " + operator + " " + R 
		window['outputBox'].update(eval(output))

	if events == sg.WIN_CLOSED:
		break

window.close()
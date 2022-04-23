import PySimpleGUI as sg

def editor(theme):
	setup = [
		[],
	]

	return sg.Window('Text Editor', setup)

window = editor('LightGrey')

while True:

	events, values = window.read()

	if events == sg.WIN_CLOSED:
		break

window.close() 
import PySimpleGUI as sg

menubox = [
	['File', ['Open','Save']],
	['Edit', ['Word Count']]
]

setup = [
	[sg.Menu(menubox, key='-menu-')],
	[sg.Text('Untitled', key='txtname')],
	[sg.Multiline(no_scrollbar = True, key='-textbox-', size=(80,40))]
]

window = sg.Window('Text Editor', setup)

while True:

	events, values = window.read()

	if events == sg.WIN_CLOSED:
		break

window.close() 
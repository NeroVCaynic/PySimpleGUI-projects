import PySimpleGUI as sg
from pathlib import Path
import os

menubox = [
	['File', ['Open','Save']],
	['Edit', ['Word Count']]
]

setup = [
	[sg.Menu(menubox, key='-menu-')],
	[sg.Text('Untitled', key='-txtname-')],
	[sg.Multiline(no_scrollbar = True, key='-txtbox-', size=(80,40))]
]

window = sg.Window('Text Editor', setup)

while True:

	events, values = window.read()

	if events == 'Open':
		filePath = sg.popup_get_file('Open', no_window=True)
		if filePath:
			file = Path(filePath)
			window['-txtbox-'].update(file.read_text())
			window['-txtname-'].update(filePath.split('/')[-1])

	if events == 'Save':
		filePath = sg.popup_get_file('Save as', no_window=True, save_as=True)
		file = Path(filePath)
		if os.path.isfile(filePath) == True:
			file.write_text(values['-txtbox-'])
			window['-txtname-'].update(filePath.split('/')[-1])

	if events == sg.WIN_CLOSED:
		break

window.close() 
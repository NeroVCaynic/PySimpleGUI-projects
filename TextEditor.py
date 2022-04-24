import PySimpleGUI as sg
from pathlib import Path
import os
from re import search

menubox = [
	['File', ['Open','Save']],
	['Edit', ['Word Count', 'Delete']]
]

txtmenu = ['emotes',['(｡◕‿‿◕｡)','(╥﹏╥)','(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄','༼ つ ◕_◕ ༽つ','୧༼ಠ益ಠ╭∩╮༽','(ㆆ _ ㆆ)']]

setup = [
	[sg.Menu(menubox, key='-menu-')],
	[sg.Text('Untitled', key='-txtname-')],
	[sg.Multiline(no_scrollbar = True, key='-txtbox-', size=(60,30), font=('Arial', 14), autoscroll=True, enable_events = True, right_click_menu=txtmenu)]
]

window = sg.Window('Text Editor', setup)

while True:

	events, values = window.read()

	if events == 'Open':
		filePath = sg.popup_get_file('Open', no_window=True)
		if filePath:
			file = Path(filePath)
			if os.path.isfile(filePath) == True:
				if search(filePath.split('/')[-1], '.txt') == True:
					window['-txtbox-'].update(file.read_text())
					window['-txtname-'].update(filePath.split('/')[-1])
				else:
					sg.Popup("Wrong File")

	if events == 'Save':
		filePath = sg.popup_get_file('Save as', no_window=True, save_as=True)
		file = Path(filePath)
		if os.path.isfile(filePath) == True:
			file.write_text(values['-txtbox-'])
			window['-txtname-'].update(filePath.split('/')[-1])

	if events == 'Word Count':
		words = values['-txtbox-'].replace('\n', ' ').split(' ')
		for count, value in enumerate(''.join(words)):
			counts = count
		sg.Popup(f'The total words are {counts+1}')


	if events == 'Delete':
		try:
			selection = window['-txtbox-'].Widget.selection_get()
			txt = values['-txtbox-'].replace('\n', ' ').split(' ')
			ind = txt.index(selection)
			txt.pop(ind)
		except:
			pass

	if events in txtmenu[1]:
		insert = values['-txtbox-'] + events
		window['-txtbox-'].update(insert)

	if events == sg.WIN_CLOSED:
		break

window.close() 
import PySimpleGUI as sg
from pathlib import Path as path
import pandas as pd

Menu = [['File', ['Open','Save as','Exit']],
	['Themes', ['Dark','Blue','Light']]
]

layout = [[sg.Menu(Menu, key='-MENU-')]]

window = sg.Window('Data Chart', layout)

while True:
	events, values = window.read()

	if events == 'Open':
		pass

	if events == 'Save as':
		pass

	if events in ['Dark','Blue','Light']:
		print(events)

	if events in [sg.WIN_CLOSED, 'Exit']:
		break

window.close()
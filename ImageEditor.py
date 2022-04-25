import PySimpleGUI as sg
import PIL as pl
from pathlib import Path
import os
from re import search

filePath = sg.popup_get_file('Open', no_window=True)
if filePath:
	file = Path(filePath)
	if os.path.isfile(filePath) == True:
		imageCol = sg.Column([[sg.Image(filePath, key='-image-')]])

comandCol = sg.Column([[sg.Slider(key='-blur-', orientation='h')],
		[sg.Slider(key='-brightness-', orientation='h')]
		]
	)

layout = [
	[comandCol, imageCol],
]

window = sg.Window("Image Editor", layout)

while True:
	events, values = window.read()

	if events == sg.WIN_CLOSED:
		break

window.close()
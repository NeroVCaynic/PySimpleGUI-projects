import PySimpleGUI as sg
import PIL as pl
from io import BytesIO
from pathlib import Path

filePath = sg.popup_get_file('Open', no_window=True)

comandCol = sg.Column([[sg.Slider(key='-blur-', orientation='h')],
		[sg.Slider(key='-brightness-', orientation='h')]
		]
	)
imageCol = sg.Column([[sg.Image(filePath, key='-image-')]])

layout = [
	[comandCol, imageCol],
]

window = sg.Window("Image Editor", layout)

while True:
	events, values = window.read()

	if events == sg.WIN_CLOSED:
		break

window.close()
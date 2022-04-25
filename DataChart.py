import PySimpleGUI as sg

layout = [
	[],
	[],
]

window = sg.Window("Data Chart", layout)

while True:
	events, values = window.read()

	if events == sg.WIN_CLOSED:
		break

window.close()
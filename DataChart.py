import PySimpleGUI as sg
import os
from pathlib import Path as path
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def csvConvert(filePath):
	csv = pd.read_csv(filePath)
	return csv


def update_figure(x, y, labelx, labely):
	plt.clf()
	plt.plot(x, y)
	plt.xlabel(labelx)
	plt.ylabel(labely)
	plt.grid(True)
	return plt.gcf()

def create_plot(fig):
	figure_canvas_agg = FigureCanvasTkAgg(fig,window['-DATACHART-'].TKCanvas)
	figure_canvas_agg.draw()
	figure_canvas_agg.get_tk_widget().pack()

def cWindow(theme='LightGrey1'):
	sg.theme(theme)

	Menu = [['File', ['Open','Save as','Exit']],
		['Themes', ['DarkGrey9','DarkGreen6','LightGrey1']]
	]

	Tab1 = sg.Tab('View', [[sg.Frame('New Entry', [[sg.Input(key='-TABLEINPUT-', expand_x = True), sg.Spin([], expand_x=True, key='-FIELD-')],
		[sg.Button('Submit', key='-TABLESUBMIT-')]], expand_x = True)], 
		[sg.Frame('Data Table', [[]], expand_x = True, expand_y = True, key='-TABLE-')]], key='-TAB1-')
	
	Tab2 = sg.Tab('Data', [[sg.Frame('Data Form', [[sg.Spin(None, key='-DATAHEADx-', expand_x = True), sg.Spin(None, key='-DATAHEADy-', expand_x = True)],
	 [sg.Button('Submit', key='-DATASUBMIT-')]], expand_x = True)],
		[sg.Frame('Data Visualization', [[sg.Canvas(size=(400,400), key='-DATACHART-')]])]
	])
	
	layout = [[sg.Menu(Menu, key='-MENU-')],
		[sg.TabGroup([[Tab1, Tab2]])]
	]

	return sg.Window('Data Chart', layout, finalize=True)

try:
	with open('Theme/Theme_Saves.json', 'r') as theme:
		themeLoad = json.load(theme)
	window = cWindow(themeLoad['Theme'])
except FileNotFoundError:
	window = cWindow()

while True:
	events, values = window.read()

	if events in ['-1-', '-2-', '-3-']:
		pass

	if events == 'Open':
		filePath = sg.popup_get_file('Open', no_window=True)
		if filePath:
			if os.path.isfile(filePath) == True:
				extension = filePath.split('/')[-1]
				if 'xlsx xml csv xls json'.find(extension.split('.')[-1]) >= 0:
					df = pd.DataFrame(csvConvert(filePath))
					newList = []
					for item in df.values.tolist():
						newList.append(item)
					window.close()
					window = cWindow(themeLoad['Theme'])
					window.extend_layout(window['-TABLE-'], [[sg.Table(values=[], headings=[item for item in df], key='-TABLECONTENT-',
						auto_size_columns=False, expand_x = True, expand_y = True, justification = "left")]])
					window['-TABLECONTENT-'].update(newList)
					window['-FIELD-'].update(values=df.columns.tolist())
					window['-DATAHEADx-'].update(values=df.columns.tolist())
					window['-DATAHEADy-'].update(values=df.columns.tolist())
				else:
					sg.Popup("Wrong File")
			else:
				sg.Popup("Wrong File")
	if events == 'Save as':
		sg.popup_get_file('Save As', save_as=True, no_window=True)

	if events in ['DarkGrey9','DarkGreen6','LightGrey1']:
		themeEvent = {'Theme':events} 
		with open('Theme/Theme_Saves.json', 'w') as theme:
			json.dump(themeEvent, theme)
		window.close()
		window = cWindow(events)

	if events == '-DATASUBMIT-':
		create_plot(update_figure(df[values['-DATAHEADx-']].tolist(),
			df[values['-DATAHEADy-']].tolist(), values['-DATAHEADx-'], 
			values['-DATAHEADy-']))

	if events in [sg.WIN_CLOSED, 'Exit']:
		break

window.close()
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

def figure(x, y, labelx, labely):
	plt.clf()
	plt.plot(x, y)
	plt.xlabel(labelx)
	plt.ylabel(labely)
	plt.grid(True)
	FigureCanvasTkAgg(plt.gcf(), window['-DATACHART-'].TKCanvas)
	figure_canvas_agg.draw()
	figure_canvas_agg.get_tk_widget().pack()

def create_canvas():
	global figure_canvas_agg
	figure_canvas_agg = FigureCanvasTkAgg(plt.gcf(),window['-DATACHART-'].TKCanvas)
	for item in figure_canvas_agg.get_tk_widget().find_all():
		figure_canvas_agg.get_tk_widget().delete(item)
	window['-DATACHART-'].TKCanvas.delete('all')
	figure_canvas_agg.draw()
	figure_canvas_agg.get_tk_widget().pack()

def cWindow(theme='LightGrey1'):
	sg.theme(theme)

	Menu = [['File', ['Open','Clear','Exit']],
		['Themes', ['DarkGrey9','DarkGreen6','LightGrey1']]
	]

	Tab1 = sg.Tab('View', [[sg.Frame('Search Entry', [[sg.Input(key='-TABLEINPUT-', expand_x = True), sg.Spin(None, size=(25), key='-FIELD-')],
		[sg.Button('Submit', key='-TABLESUBMIT-')]], expand_x = True, key='-SEARCHFRAME-', visible = False)], 
		[sg.Frame('Data Table', [[]], expand_x = True, expand_y = True, key='-TABLE-')]], key='-TAB1-')
	
	Tab2 = sg.Tab('Data', [[sg.Frame('Data Form', [[sg.Spin(None, key='-DATAHEADx-', size=(45)), sg.Spin(None, key='-DATAHEADy-', size=(45))],
	 [sg.Button('Submit', key='-DATASUBMIT-')]], expand_x = True, key='-VISUALINPUT-', visible = False)],
		[sg.Frame('Data Visualization', [[sg.Canvas(size=(400,400), expand_x=True, expand_y=True, key='-DATACHART-')]], expand_x=True, expand_y=True)]
	])
	
	layout = [[sg.Menu(Menu, key='-MENU-')],
		[sg.TabGroup([[Tab1, Tab2]])]
	]

	return sg.Window('Data View & Visualizer', layout, finalize=True)

try:
	with open('Theme/Theme_Saves.json', 'r') as theme:
		themeLoad = json.load(theme)
	window = cWindow(themeLoad['Theme'])
	create_canvas()
except FileNotFoundError:
	window = cWindow()
	create_canvas()

while True:
	events, values = window.read()

	if events == '-TABLESUBMIT-' and values['-FIELD-'] != "":
		if values['-TABLEINPUT-'] != "" or " ":
			try:
				try:
					newDF = pd.DataFrame(df.loc[df[values['-FIELD-']] == int(values['-TABLEINPUT-'])])
				except KeyError:
					pass
			except ValueError:
				try:
					newDF = pd.DataFrame(df.loc[df[values['-FIELD-']] == values['-TABLEINPUT-']])
				except KeyError:
					pass
			try:
				sg.Popup("\n".join(map(str, newDF.values.tolist())))
			except NameError:
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
					create_canvas()
					window['-SEARCHFRAME-'].update(visible = True)
					window['-VISUALINPUT-'].update(visible = True)
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
	if events == 'Clear':
		clear = sg.popup_yes_no("Are you sure you want to clear?")
		if clear == 'Yes':
			window.close()
			try:
				window = cWindow(themeLoad['Theme'])
				create_canvas()
			except FileNotFoundError:
				window = cWindow()
				create_canvas()

	if events in ['DarkGrey9','DarkGreen6','LightGrey1']:
		themeEvent = {'Theme':events} 
		with open('Theme/Theme_Saves.json', 'w') as theme:
			json.dump(themeEvent, theme)
		window.close()
		window = cWindow(events)
		create_canvas()

	if events == '-DATASUBMIT-':
		try:
			figure(df[values['-DATAHEADx-']].tolist(),df[values['-DATAHEADy-']].tolist(), 
				values['-DATAHEADx-'], values['-DATAHEADy-'])
		except KeyError:
			sg.Popup("Invalid")

	if events in [sg.WIN_CLOSED, 'Exit']:
		break

window.close()
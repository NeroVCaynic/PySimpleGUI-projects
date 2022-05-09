import PySimpleGUI as sg
import os
from pathlib import Path as path
import pandas as pd
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_figure():
	axes = fig.axes
	x = [100, 200, 300, 400]
	y = [10, 250, 300, 400]
	axes[0].plot(x,y,'r-')
	figure_canvas_agg.draw()
	figure_canvas_agg.get_tk_widget().pack()

def create_plot():
	global fig, figure_canvas_agg
	fig = plt.figure.Figure(figsize = (5,4))
	fig.add_subplot(111).plot([],[])
	figure_canvas_agg = FigureCanvasTkAgg(fig,window['-DATACHART-'].TKCanvas)
	figure_canvas_agg.draw()
	figure_canvas_agg.get_tk_widget().pack()

def cWindow(theme='LightGrey1'):
	sg.theme(theme)

	Menu = [['File', ['Open','Save as','Exit']],
		['Themes', ['DarkGrey9','DarkGreen6','LightGrey1']]
	]

	heading = ['int','string','boolean']
	content = [[1,'a',True],[2,'b',False],[3,'c',True]]

	Tab1 = sg.Tab('View', [[sg.Frame('New Entry', [[sg.Input(key='-TABLEINPUT-', expand_x = True), sg.Spin(heading, expand_x=True)],
		[sg.Button('Submit', key='-TABLESUBMIT-')]], expand_x = True)],
		[sg.Frame('Data Table', [[sg.Table(values=content, headings=heading, 
			key='-TABLECONTENT-', auto_size_columns=True, expand_x = True, expand_y = True, justification = "left",)]], expand_x = True, expand_y = True)]
	])
	
	Tab2 = sg.Tab('Data', [[sg.Frame('Data Form', [[sg.Spin(heading, key='-DATAHEADx-', expand_x = True), sg.Spin(heading, key='-DATAHEADy-', expand_x = True), 
		sg.Spin(['Plot', 'Pie', 'Bar'],
	 expand_x = True)], [sg.Button('Submit', key='-DATASUBMIT-')]], expand_x = True)],
		[sg.Frame('Data Visualization', [[sg.Canvas(size=(400,400), key='-DATACHART-')]])]
	])
	
	layout = [[sg.Menu(Menu, key='-MENU-')],
		[sg.TabGroup([[Tab1, Tab2]])]
	]

	return sg.Window('Data Chart', layout, finalize=True)

window = cWindow()

create_plot()

while True:
	events, values = window.read()

	if events in ['-1-', '-2-', '-3-']:
		pass

	if events == 'Open':
		filePath = sg.popup_get_file('Open', no_window=True)
		if filePath:
			if os.path.isfile(filePath) == True:
				extension = filePath.split('/')[-1]
				if extention.split('.')[-1] in ['xlsx', 'xml', 'csv', 'xls', 'json'] == True:
					window['-TABLETITLE-'].update()
					window['-TABLECONTENT-'].update()
				else:
					sg.Popup("Wrong File")

	if events == 'Save as':
		sg.popup_get_file('Save As', save_as=True, no_window=True)

	if events in ['DarkGrey9','DarkGreen6','LightGrey1']:
		window.close()
		window = cWindow(events)
		create_plot()

	if events == '-DATASUBMIT-':
		update_figure()

	if events in [sg.WIN_CLOSED, 'Exit']:
		break

window.close()
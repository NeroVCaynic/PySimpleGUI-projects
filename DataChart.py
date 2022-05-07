import PySimpleGUI as sg
import os
from pathlib import Path as path
import pandas as pd
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_figure(data):
	axes = fig.axes
	x = [i[0] for i in data]
	y = [int(i[1]) for i in data]
	axes[0].plot(x,y,'r-')
	figure_canvas_agg.draw()
	figure_canvas_agg.get_tk_widget().pack()

def cWindow(theme='LightGrey'):
	sg.theme(theme)

	Menu = [['File', ['Open','Save as','Exit']],
		['Themes', ['Dark','Blue','LightGrey']]
	]

	Tab1 = sg.Tab('View', [[sg.Text('', key='-TABLETEXT-')],
		[sg.Button('Button', key='-BUTTON-')],
		[sg.Frame('Data Table', [[sg.Table(values=[[1,'a',True],[2,'b',False],[3,'c',True]], headings=['int','string','boolean'], 
			key='-TABLECONTENT-', auto_size_columns=True, expand_x = True, expand_y = True, justification = "left",)]], expand_x = True, expand_y = True)]
	])
	
	Tab2 = sg.Tab('Data', [[sg.Checkbox('1', key='-1-'), sg.Checkbox('2', key='-2-'), sg.Checkbox('3', key='-3-')],
		[sg.Frame('Data Visualization', [[sg.Canvas(size=(400,400), key='-CHART-')]])]
	])
	
	layout = [[sg.Menu(Menu, key='-MENU-')],
		[sg.TabGroup([[Tab1, Tab2]])]
	]

	return sg.Window('Data Chart', layout, finalize=True)

window = cWindow()

fig = plt.figure.Figure(figsize = (5,4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig,window['-CHART-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

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

	if events in ['Dark','Blue','LightGrey']:
		window.close()
		window = cWindow(events)

	if events in [sg.WIN_CLOSED, 'Exit']:
		break

window.close()
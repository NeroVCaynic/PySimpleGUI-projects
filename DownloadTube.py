import PySimpleGUI as sg
from pytube import YouTube

sg.theme('DarkRed1')
layout = [
	[sg.TabGroup(
		[[sg.Tab('Tab1',[[sg.Text('Link:'), sg.Input(key='-link-'), sg.Button('Submit', key='-submit-')],
			[sg.Button('Highest Quality', key='-highQ-', pad=(5,40)), sg.Text('Quality', key='HQ')], 
			[sg.Button('Lowest Quality', key='-lowQ-', pad=(5,40)), sg.Text('Quality', key='LQ')], 
			[sg.Button('Audio', key='-audio-', pad=(5,40)), sg.Text('Audio', key='AQ')],
			[sg.VPush()]]), 
		sg.Tab('Tab2',[[sg.Text('Title: ',key='-title-')],
			[sg.Text('Length:'),sg.Text('', key='-length-')],
			[sg.Text('Views:'),sg.Text('', key='-views-')],
			[sg.Text('Author:'),sg.Text('', key='-author-')],
			[sg.Text('Description:')],
			[sg.Multiline('', key ='-desc-', expand_x=True, expand_y=True, no_scrollbar=True, disabled=True)]])]])]
]
window = sg.Window('DownloadTube', layout)

while True:
	events, values = window.read()

	if events == sg.WIN_CLOSED:
		break

window.close()
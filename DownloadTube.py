import PySimpleGUI as sg
from pytube import YouTube
import validators as val

def progressCheck(stream, chunk, bytes_remaining):
	window['-downProg-'].update(100 - round(bytes_remaining / stream.filesize * 100))

def onComplete(stream, file_path):
	window['-downProg-'].update(0)

sg.theme('DarkRed1')
layout = [
	[sg.TabGroup(
		[[sg.Tab('Download',[[sg.Text('Link:'), sg.Input(key='-link-'), sg.Button('Submit', key='-submit-')],
			[sg.Button('Highest Quality', key='-highQ-', pad=(5,40)), sg.Text('Quality', key='-HQ-')], 
			[sg.Button('Lowest Quality', key='-lowQ-', pad=(5,40)), sg.Text('Quality', key='-LQ-')], 
			[sg.Button('Audio', key='-audio-', pad=(5,40)), sg.Text('Audio', key='-AQ-')],
			[sg.VPush()],
			[sg.Progress(100,orientation='h', size=(20, 20), key='-downProg-', expand_x = True)]]),
		sg.Tab('Info',[[sg.Text('Title: ',key='-title-')],
			[sg.Text('Length:'),sg.Text('', key='-length-')],
			[sg.Text('Views:'),sg.Text('', key='-views-')],
			[sg.Text('Author:'),sg.Text('', key='-author-')],
			[sg.Text('Description:')],
			[sg.Multiline('', key ='-desc-', expand_x=True, expand_y=True, no_scrollbar=True, disabled=True)]])]])]
]
window = sg.Window('DownloadTube', layout)

while True:
	events, values = window.read()
	
	if events == '-submit-':
		valid=val.url(values['-link-'])
		if valid==True:	
				linkGot = YouTube(values['-link-'], on_progress_callback=progressCheck, on_complete_callback=onComplete)
				window['-title-'].update(f'Title: {linkGot.title}')
				window['-length-'].update(f'{round(linkGot.length/60, 2)} minutes')
				window['-views-'].update(linkGot.views)
				window['-author-'].update(linkGot.author)
				window['-desc-'].update(linkGot.description)
				window['-HQ-'].update(f'{round(linkGot.streams.get_highest_resolution().filesize / 1048576,1)} MB')
				window['-LQ-'].update(f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576,1)} MB')
				window['-AQ-'].update(f'{round(video_object.streams.get_audio_only().filesize / 1048576,1)} MB')
				
		else:
			sg.Popup('invalid URL')

		if events == '-highQ-':
			linkGot.streams.get_highest_resolution().download()

		if events == '-lowQ-':
			linkGot.streams.get_lowest_resolution().download()

		if events == '-audio-':
			linkGot.streams.get_audio_only().download()

	if events == sg.WIN_CLOSED:
		break

window.close()
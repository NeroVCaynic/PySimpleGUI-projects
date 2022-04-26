import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
from pathlib import Path

def update_image(ogImage,blur,contrast,emboss,contour,flipx,flipy):
	global image
	image = ogImage.filter(ImageFilter.GaussianBlur(blur))
	image = image.filter(ImageFilter.UnsharpMask(contrast))

	if emboss:
		image = image.filter(ImageFilter.EMBOSS())
	if contour:
		image = image.filter(ImageFilter.CONTOUR())

	if flipx:
		image = ImageOps.mirror(image)
	if flipy:
		image = ImageOps.flip(image)

	bio = BytesIO()
	image.save(bio, format = 'PNG')

	window['-image-'].update(data = bio.getvalue())

filePath = sg.popup_get_file('Open', no_window=True)

comandCol = sg.Column([[sg.Frame('Blur',layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-blur-')]])],
	[sg.Frame('Contrast',layout = [[sg.Slider(range = (0,10), orientation = 'h', key = '-contrast-')]])],
	[sg.Checkbox('Emboss', key = '-embross-'), sg.Checkbox('Contour', key = '-contour-')],
	[sg.Checkbox('Flip X', key = '-flipX-'), sg.Checkbox('Flip Y', key = '-flipY-')],
	[sg.Button('Save image', key = '-save-')]])

try:
	ogImage = Image.open(filePath)
	imageCol = sg.Column([[sg.Image(Image.open(filePath), key='-image-')]])
except AttributeError:
	pass


try:
	layout = [
		[comandCol, imageCol],
	]

	window = sg.Window("Image Editor", layout)

	while True:
		events, values = window.read(timeout=50)

		try:
			update_image(
				ogImage, 
				values['-blur-'],
				values['-contrast-'], 
				values['-embross-'], 
				values['-contour-'],
				values['-flipX-'],
				values['-flipY-']
			)
		except TypeError:
			pass

		if events == '-save-':
			savePath = sg.popup_get_file('Save',save_as = True, no_window = True) + '.png'
			image.save(save_path,'PNG')

		if events == sg.WIN_CLOSED:
			break

	window.close()
except NameError:
	pass
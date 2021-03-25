from PIL import Image, ImageDraw, ImageFont
import pyfiglet
from time import sleep
from pathlib import Path
import textwrap
counter = 0

#draw description text block wrd by wrd
text = []
line = ' '
lineStr = ' '
i = 0
y = 0
textHeight = 0
lineCounter = 0
height = 0
textY = 0
wrapped_text = ' '
input_array = ['avant la lettre :', 'media archaeology cn', '20210320', '10:30AM CST','20210319', '20:30PM MST']


def makeSequence(input, textY, saveName):
	#draw title text block 
	out = Image.new('RGB', (900,1200), (255,255,255))
	font = 	ImageFont.truetype('/Users/biyiwen/Documents/avant_la_lettre_poster_generation/fonts/bitfont.ttf', size=15)

	d = ImageDraw.Draw(out)
	textHeight = font.getsize(input)[1]
	print(textHeight)
	textY = textHeight * lineCounter*1.2 + 480
	d.text((10,textY), input, (0,0,0), font=font)
	saveName = 'line' + '%04d' %lineCounter + '.png'
	out.save(saveName)

def makeFiglet(input, y):
	figletText = pyfiglet.figlet_format(input)
	out_figlet = Image.new('RGB',(900,1200),(255,255,255))
	d_figlet = ImageDraw.Draw(out_figlet)
	d_figlet.text((10,y), figletText,(0,0,0))
	save_name = str(input) + '.png'
	out_figlet.save(save_name)

for i in input_array:
	makeFiglet(i, counter * 80)
	counter += 1 

with open ('description.txt', 'r') as f:
	text = f.read()
	wrapper = textwrap.wrap(text, width=50)

for line in wrapper:
	#print(line)
	lineCounter += 1
	#print(lineCounter)
	makeSequence(line, textY, lineCounter)


	




	
       
	
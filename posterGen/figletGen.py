import pyfiglet
from time import sleep
from pathlib import Path

title = 'avant la lettre'
subtitle = 'media archaeology cn'
description = Path('description.txt').read_text()
date = '2020MAR12 1930MST\n2020MAR13 1030CST'

interval = 1

#description is in plain text
def insertText():
	blkTitle = pyfiglet.figlet_format(title, font = 'slant')
	blkSubtitle = pyfiglet.figlet_format(subtitle)
	blkDescription = description
	blkTime = pyfiglet.figlet_format(date, font = 'smkeyboard')

	print (blkTitle)
	sleep(interval)

	print (blkSubtitle)
	sleep(interval)

	splitText(description)
	#hard coded in a line break
	print ('')
	print ('')
	
	print (blkTime)
	sleep(interval)

def splitText(input):
	splitText = input.split()
	for wrd in splitText:
		print(wrd, flush=True, end = ' ')
		sleep(interval/10)

def main ():
		insertText()

if __name__ == '__main__':
		main()


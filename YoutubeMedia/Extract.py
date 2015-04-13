#!/usr/local/bin/python
# change above line to point to local python executable

#Prerequisites
# youtube-dl @ http://rg3.github.io/youtube-dl/

import string
from subprocess import call

import urllib2
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError

print""
print "It is all fun and games until someone gets hacked!"
print"          _                      _          "
print"   _     /||       .   .        ||\     _   "
print"  ( }    \||D    '   '     '   C||/    { %  "
print" | /\__,=_[_]   '  .   . '       [_]_=,__/\ |"
print" |_\_  |----|                    |----|  _/_|"
print" |  |/ |    |                    |    | \|  |"
print" |  /_ |    |                    |    | _\  |"
print""

print "This script accepts a will take a text file that contains links the"
print "DEFCON videos on YouTube and download them to your local machine."
print""

def get_file():
	try:
		txtFile = str(raw_input('Enter path and file name: '))
		if not txtFile:
			raise ValueError('No path and/or file was provided! What were you expecting?')
		else:
			print txtFile
			execute_rip(txtFile)
	except ValueError as e:
		print(e)
		exit()

def execute_rip(txtFile):
	command = "youtube-dl --batch-file=" + txtFile + " -o ~/Downloads/%(uploader)s/%(title)s-%(id)s.%(ext)s"
	call(command.split(), shell=False)

get_file()

### Done!
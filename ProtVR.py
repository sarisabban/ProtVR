#!/usr/bin/python3

# Author: Sari Sabban
# Email:  sari.sabban@gmail.com
# URL:    https://github.com/sarisabban
#
# Created By:   	Sari Sabban
# Created Date: 	13 March 2017

import sys
import re
import urllib
import Bio
import os
from Bio.PDB import *

if sys.argv[1]=='-d':
	print('Downloading',sys.argv[2],'from http://rcsb.org')
	filename=urllib.request.urlopen('http://files.rcsb.org/view/'+sys.argv[2]+'.pdb')
else:
	filename=open(sys.argv[1])

#print('Calculating...')

data=open('code.html','w')

data.write('<script src="https://aframe.io/releases/0.5.0/aframe.min.js"></script>\n')
data.write('<a-scene>\n')
data.write('\t<a-sky color="#111111"></a-sky>\n')

for line in filename:
	line=line.decode()
	if line.startswith('ATOM'):
		splitline=line.split()
		try:
			coordinates=(splitline[11],splitline[6],splitline[7],splitline[8])
		except:
			coordinates=(splitline[10],splitline[6],splitline[7],splitline[8])
		#Convert PyMOL colurs to HEX: (225)*(Pymol Colour Value) https://pymolwiki.org/index.php/Color_Values
		if coordinates[0]=='N':
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#2D2DE1"></a-sphere>\n'
		elif coordinates[0]=='C':
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#2DE12D"></a-sphere>\n'
		elif coordinates[0]=='O':
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#E14343"></a-sphere>\n'
		elif coordinates[0]=='H':
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#CBCBCB"></a-sphere>\n'
		elif coordinates[0]=='S':
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#CBAE38"></a-sphere>\n'
		elif coordinates[0]=='I':
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#830083"></a-sphere>\n'
		else:
			js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#6F6F6F"></a-sphere>\n'
		x=' '.join(js)
		data.write(x)

data.write('</a-scene>')
data.close()

print('Done')

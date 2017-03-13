#!/usr/bin/python3

# Author: Sari Sabban
# Email:  sari.sabban@gmail.com
# URL:    https://github.com/sarisabban
#
# Created By:   	Sari Sabban
# Created Date: 	13 March 2017

import sys
import re

filename=open(sys.argv[1])

print('<script src="https://aframe.io/releases/0.5.0/aframe.min.js"></script>')
print('<a-scene>')
print('\t','<a-sky color="#111111"></a-sky>')

for line in filename:
	if line.startswith('ATOM'):
		splitline=line.split()
		coordinates=(splitline[11],splitline[6],splitline[7],splitline[8])
		#Convert PyMOL colurs to HEX: (225)*(Pymol Colour Value) https://pymolwiki.org/index.php/Color_Values
		if coordinates[0]=='N':
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#2D2DE1"></a-sphere>')
		elif coordinates[0]=='C':
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#2DE12D"></a-sphere>')
		elif coordinates[0]=='O':
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#E14343"></a-sphere>')
		elif coordinates[0]=='H':
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#CBCBCB"></a-sphere>')
		elif coordinates[0]=='S':
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#CBAE38"></a-sphere>')
		elif	coordinates[0]=='I':
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#830083"></a-sphere>')
		else:
			print('\t','<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#6F6F6F"></a-sphere>')
print('</a-scene>')

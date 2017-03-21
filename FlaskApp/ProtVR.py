# Author: Sari Sabban
# Email:  sari.sabban@gmail.com
# URL:    https://github.com/sarisabban
#
# Created By:   	Sari Sabban
# Created Date: 	20 March 2017

import urllib

def ProtVR(x):
	lis=list() 
	filename='HELLO C '
	filename=urllib.urlopen('http://files.rcsb.org/view/'+x+'.pdb')
	lis.append('<script src="/static/aframe.min.js"></script>\n')
	lis.append('<a-scene>\n')
	lis.append('\t<a-sky color="#111111"></a-sky>\n')
	for line in filename:
		line=line.decode()
		if line.startswith('ATOM'):
			splitline=line.split()
			try:
				coordinates=(splitline[11],splitline[6],splitline[7],splitline[8])
			except:
				coordinates=(splitline[10],splitline[6],splitline[7],splitline[8])
			if coordinates[0]=='N':
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#2D2DE1"></a-sphere>'
			elif coordinates[0]=='C':
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#2DE12D"></a-sphere>'
			elif coordinates[0]=='O':
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#E14343"></a-sphere>'
			elif coordinates[0]=='H':
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#CBCBCB"></a-sphere>'
			elif coordinates[0]=='S':
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#CBAE38"></a-sphere>'
			elif coordinates[0]=='I':
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#830083"></a-sphere>'
			else:
				js='\t<a-sphere position="',coordinates[1],coordinates[2],coordinates[3],'" radius="1" color="#6F6F6F"></a-sphere>'
			result=' '.join(js)
			lis.append(result)
	lis.append('</a-scene>')
	final=' '.join(lis)
	return(final)
	#print(final)

#ProtVR('2HIU')

# coding: utf-8

from textutilities import strip_accents

def filesToProcess():
	import glob
	return glob.glob("contempworks*.xml")

def parseFile(fileName):
	from xml.dom.minidom import parseString
	file = open(fileName, 'r')
	data = file.read()
	file.close()
	dom = parseString(data)
	return dom

def processDom(dom):
	composers = dom.getElementsByTagName('composer')
	if composers:
		for composer in composers:
			name = composer.attributes["name"].value
			surname = composer.attributes["surname"].value
			print(strip_accents(name) + " " + strip_accents(surname))	

files = filesToProcess()
for f in files:
	dom = parseFile(f)
	processDom(dom)
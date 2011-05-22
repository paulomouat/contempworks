# coding: utf-8

from entities import *
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
	composersXml = dom.getElementsByTagName('composer')
	if composersXml:
		for composerXml in composersXml:
			processComposerXml(composerXml)

def processComposerXml(composerXml):
	composer = Composer()
	name = composerXml.attributes["name"].value
	surname = composerXml.attributes["surname"].value
	born = composerXml.attributes["born"].value
	died = composerXml.attributes["died"].value
	composer.name = name
	composer.surname = surname
	composer.born = born
	composer.died = died
	print composer.display()
	#print strip_accents(name) + " " + strip_accents(surname)	
	

files = filesToProcess()
for f in files:
	dom = parseFile(f)
	processDom(dom)
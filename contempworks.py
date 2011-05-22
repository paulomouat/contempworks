# coding: utf-8

from entities import *
from textutilities import strip_accents
from xmlutilities import *

def filesToProcess():
	import glob
	return glob.glob("contempworks-o.xml")

def parseFile(fileName):
	from xml.dom.minidom import parseString
	file = open(fileName, 'r')
	data = file.read()
	file.close()
	dom = parseString(data)
	return dom

def readDom(dom):
	composers = dom.getElementsByTagName('composer')
	readComposers(composers)

def readComposers(composers):
	if composers:
		for composer in composers:
			readComposer(composer)

def readComposer(node):
	composer = Composer()
	name = getAttributeValue(node, "name")
	surname = getAttributeValue(node, "surname")
	born = getAttributeValue(node, "born")
	died = getAttributeValue(node, "died")
	composer.name = name
	composer.surname = surname
	composer.born = born
	composer.died = died
	readCompositions(node, composer)
	print composer.display()
	
def readCompositions(node, composer):
	compositions = selectChildren(node, "composition")
	for composition in compositions:
		readComposition(composition, composer)
		
def readComposition(node, composer):
	composition = Composition()
	name = selectSingleChildValue(node, "name")
	composition.name = name
	descriptions = selectChildren(node, "description")
	if descriptions:
		for description in descriptions:
			text = getTextValue(description)
			composition.descriptions.append(text)
	composer.compositions.append(composition)

files = filesToProcess()
for f in files:
	dom = parseFile(f)
	readDom(dom)
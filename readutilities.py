from entities import *
from textutilities import strip_accents
from xmlutilities import *

def filesToProcess():
	import glob
	return glob.glob("contempworks-*.xml")

def parseFile(fileName):
	from xml.dom.minidom import parseString
	file = open(fileName, 'r')
	data = file.read()
	file.close()
	dom = parseString(data)
	return dom

def readDom(dom):
	composerNodes = dom.getElementsByTagName('composer')
	return readComposers(composerNodes)

def readComposers(composerNodes):
	composers = []
	if composerNodes:
		for composerNode in composerNodes:
			composer = readComposer(composerNode)
			composers.append(composer)
	return composers

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
	composer.compositions = readCompositions(node)
	return composer
	
def readCompositions(node):
	compositions = selectChildren(node, "composition")
	results = []
	for composition in compositions:
		c = readComposition(composition)
		results.append(c)
	return results
		
def readComposition(node):
	composition = Composition()
	composition.name = readValue(node, "name")
	composition.descriptions = readDescriptions(node)
	composition.length = readValue(node, "length")
	composition.parts = readParts(node)
	composition.participants = readParticipants(node)
	composition.composed = readComposed(node)
	composition.recorded = readRecorded(node)
	composition.release = readValue(node, "release")
	composition.released = readValue(node, "released")
	return composition

def readDescriptions(node):
	descriptions = selectChildren(node, "description")
	results = []
	if descriptions:
		for description in descriptions:
			text = getTextValue(description)
			results.append(text)	
	return results

def readParts(node):
	partNodes = selectChildren(node, "part")
	results = []
	if partNodes:
		for partNode in partNodes:
			part = readPart(partNode)
			results.append(part)
	return results

def readPart(node):
	part = Part()
	part.number = readValue(node, "number")
	part.name = readValue(node, "name")
	part.description = readValue(node, "description")
	part.length = readValue(node, "length")
	part.participants = readParticipants(node)
	part.composed = readComposed(node)
	part.recorded = readRecorded(node)
	return part

def readParticipants(node):
	participantNodes = selectChildren(node, ["instrument", "player", "conductor"])
	results = []
	if participantNodes:
		for participantNode in participantNodes:
			participant = None
			if participantNode.nodeName == "instrument":
				participant = readInstrument(participantNode)
			elif participantNode.nodeName == "player":
				participant = readPlayer(participantNode)
			elif participantNode.nodeName == "conductor":
				participant = readConductor(participantNode)
			if participant:
				results.append(participant)
	return results

def readInstrument(node):
	instrument = Instrument()
	instrument.name = getAttributeValue(node, "name")
	instrument.players = readPlayers(node)
	return instrument

def readPlayers(node):
	playerNodes = selectChildren(node, "player")
	results = []
	if playerNodes:
		for playerNode in playerNodes:
			results.append(readPlayer(playerNode))
	return results

def readPlayer(node):
	player = Player()
	player.name = getAttributeValue(node, "name")
	return player

def readConductor(node):
	conductor = Conductor()
	conductor.name = getTextValue(node)
	return conductor

def readComposed(node):
	composed = selectSingleChild(node, "composed")
	period = ComposedPeriod()
	period.start = getAttributeValue(composed, "start")
	period.end = getAttributeValue(composed, "end")
	return period
	
def readRecorded(node):
	recorded = selectSingleChild(node, "recorded")
	period = RecordedPeriod()
	period.start = getAttributeValue(recorded, "start")
	period.end = getAttributeValue(recorded, "end")
	return period

def readAll():
	composers = []
	files = filesToProcess()
	for f in files:
		try:
			dom = parseFile(f)
			composers.extend(readDom(dom))
		except Exception as e:
			print("Error in file ", f)
			raise e
	return composers
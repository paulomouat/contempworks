# coding: utf-8

from textutilities import *
from htmltemplates import *
from entities import *

def generateComposerList(composers):
	fileName = "generated/composerlist.html"
	header = open("composerlist-header.html")
	footer = open("composerlist-footer.html")
	contents = header.read()
	header.close()
	
	previous = " "
	for composer in composers:
		current = composer.surname[0]
		if current != previous:
			contents += generateInitialRow(current)
			previous = current
		contents += generateComposerInList(composer)
	contents += footer.read()
	footer.close()
		
	output = open(fileName, "w")
	output.write(contents)
	output.close()

def generateInitialRow(initial):
	row = initialRow.format(initial=initial)
	return row

def generateComposerInList(composer):
	fileName = getFileName(composer)
	row = composerListRow.format(filename=fileName, surname=htmlEscape(composer.surname), name=htmlEscape(composer.name), born=composer.born, died=composer.died)
	return row

def generateComposerTitle(composer):
	row = composerTitleRow.format(surname=htmlEscape(composer.surname), name=htmlEscape(composer.name),
		born=composer.born, died=composer.died)
	return row
	
def generateCompositions(composer):
	rows = ""
	for composition in composer.compositions:
		rows += generateComposition(composition)
	return rows
	
def generateComposition(composition):
	nameHtml = compositionNameRow.format(name=htmlEscape(composition.name))
	descriptionsHtml = ""
	for description in composition.descriptions:
		descriptionsHtml += compositionDescriptionRow.format(description=htmlEscape(description))
	lengthHtml = compositionLengthRow.format(length=composition.length)
	partsHtml = ""
	for part in composition.parts:
		number = ""
		if part.number:
			number = part.number
		name = ""
		if part.name:
			name = htmlEscape(part.name)
		length = ""
		if part.length:
			length = part.length
		description = ""
		if part.description:
			description = htmlEscape(part.description)
		if part.composed:
			composed = generateComposed(part.composed)
		else:
			composed = ""
		partsHtml += compositionPartRow.format(number=number, name=name, length=length, description=description, composed=composed)
	participantsHtml = generateParticipants(composition.participants)
	composedHtml = generateComposed(composition.composed)
	recordedHtml = generateRecorded(composition.recorded)
	releaseHtml = htmlEscape(composition.release)
	releasedHtml = htmlEscape(composition.released)
	row = compositionRow.format(name=nameHtml, descriptions=descriptionsHtml, length=lengthHtml, parts=partsHtml,
		participants=participantsHtml, composed=composedHtml, recorded=recordedHtml, release=releaseHtml, released=releasedHtml)
	return row

def generateParticipants(participants):
	row = ""
	for participant in participants:
		if isinstance(participant, Conductor):
			name = htmlEscape(participant.name)
			conductorRow = compositionConductorRow.format(name=name)
			row += compositionParticipantRow.format(participant=conductorRow)
		elif isinstance(participant, Player):
			name = htmlEscape(participant.name)
			playerRow = name
			row += compositionParticipantRow.format(participant=playerRow)
		elif isinstance(participant, Instrument):
			name = htmlEscape(participant.name)
			players = ""
			for player in participant.players:
				playerName = htmlEscape(player.name)
				players += playerName + ", "
			instrumentRow = compositionInstrumentRow.format(name=name, players=players)
			row += compositionParticipantRow.format(participant=instrumentRow)
	return row

def generateComposed(composed):
	start = composed.start
	end = composed.end
	if not composed.start:
		start = "?"
	v = start;
	if composed.end:
		v += "-" + composed.end
	row = compositionComposedRow.format(composed=htmlEscape(v))
	return row

def generateRecorded(recorded):
	start = recorded.start
	end = recorded.end
	if not recorded.start:
		start = "?"
	v = start;
	if recorded.end:
		v += "-" + recorded.end
	return htmlEscape(v)

def generateComposerFiles(composers):
	for composer in composers:
		generateComposerFile(composer)

def generateComposerFile(composer):
	fileName = "generated2/" + getFileName(composer)
	output = open(fileName, "w")
	titleHtml = generateComposerTitle(composer)
	compositionsHtml = generateCompositions(composer)
	contents = composerFileTemplate.format(composerTitle=titleHtml, compositions=compositionsHtml)
	output.write(contents)
	output.close()

def getFileName(composer):
	rawname = composer.surname + composer.name
	escaped = safe(rawname)
	lowered = escaped.lower()
	return lowered + ".html"

def safe(rawtext):
	escaped = strip_accents(rawtext)
	escaped = escaped.replace(" ", "-")
	return escaped
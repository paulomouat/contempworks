# coding: utf-8

from textutilities import *
from htmltemplates import *
from entities import *
import codecs
import functools

def generateComposerList(composers):
    fileName = "generated/composerlist.html"
    contents = ""
    previous = " "
    for composer in composers:
        current = composer.surname[0]
        if current != previous:
            contents += generateInitialRow(current)
            previous = current
        contents += generateComposerInList(composer)
    contents = composerListTemplate.format(composerList=contents)
    output = codecs.open(fileName, "w", "utf-8")
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
	compositions = sorted(composer.compositions, key = functools.cmp_to_key(sortCompositionsByEnd))
	compositions = sorted(compositions, key = functools.cmp_to_key(sortCompositionsByStart))
	for composition in compositions:
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
		composed = ""
		if part.composed:
			composed = generateComposed(part.composed)
		participants = ""
		if part.participants:
			participants = generatePartParticipants(part.participants)
		partsHtml += compositionPartRow.format(number=number, name=name, length=length, description=description, composed=composed, participants=participants)
	participantsHtml = generateParticipants(composition.participants)
	composedHtml = generateComposed(composition.composed)
	if composedHtml == "":
		composedHtml = "(?)"
	recordedHtml = generateRecorded(composition.recorded)
	releaseHtml = htmlEscape(composition.release)
	releasedHtml = htmlEscape(composition.released)
	row = compositionRow.format(name=nameHtml, descriptions=descriptionsHtml, length=lengthHtml, parts=partsHtml,
		participants=participantsHtml, composed=composedHtml, recorded=recordedHtml, release=releaseHtml, released=releasedHtml)
	return row

def generatePartParticipants(participants):
	row = ""
	partParticipantRows = generateParticipants(participants, indent="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
	row += partParticipantRow.format(participant=partParticipantRows)
	return row

def generateParticipants(participants, indent=""):
	row = ""
	for participant in participants:
		if isinstance(participant, Conductor):
			name = htmlEscape(participant.name)
			conductorRow = compositionConductorRow.format(name=name)
			row += indent + compositionParticipantRow.format(participant=conductorRow)
		elif isinstance(participant, Player):
			name = htmlEscape(participant.name)
			playerRow = name
			row += indent + compositionParticipantRow.format(participant=playerRow)
		elif isinstance(participant, Instrument):
			name = htmlEscape(participant.name)
			players = ""
			for player in participant.players:
				playerName = htmlEscape(player.name)
				players += playerName + ", "
			instrumentRow = compositionInstrumentRow.format(name=name, players=players)
			row += indent + compositionParticipantRow.format(participant=instrumentRow)
	return row

def generateComposed(composed):
	start = composed.start
	end = composed.end
	if not composed.start:
		start = "?"
	result = start
	if composed.end:
		result += "-" + composed.end
	row = ""
	if result != "?":
		row = compositionComposedRow.format(composed=htmlEscape(result))
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
	fileName = "generated/" + getFileName(composer)
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

def sortCompositionsByStart(compositionA, compositionB):
	composedA = compositionA.composed
	yearA = ""
	if composedA:
		startA = composedA.start
		endA = composedA.end
		if startA:
			yearA = startA
		elif endA:
			yearA = endA
			
	composedB = compositionB.composed
	yearB = ""
	if composedB:
		startB = composedB.start
		endB = composedB.end
		if startB:
			yearB = startB
		elif endB:
			yearB = endB

	if yearA < yearB:
		return -1
	else:
		return 1

	#return yearA - yearB
	
def sortCompositionsByEnd(compositionA, compositionB):
	composedA = compositionA.composed
	yearA = ""
	if composedA:
		startA = composedA.start
		endA = composedA.end
		if endA:
			yearA = endA
		elif startA:
			yearA = startA
			
	composedB = compositionB.composed
	yearB = ""
	if composedB:
		startB = composedB.start
		endB = composedB.end
		if endB:
			yearB = endB
		elif startB:
			yearB = startB
		
	if yearA < yearB:
		return -1
	else:
		return 1

	#return yearA - yearB
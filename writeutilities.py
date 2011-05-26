# coding: utf-8

from textutilities import *
from htmltemplates import *

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
		partsHtml += compositionPartRow.format(number=part.number, name=htmlEscape(part.name), length=part.length,
			description=htmlEscape(part.description), composed=generateComposed(part.composed))
	participantsHtml = ""
	composedHtml = ""
	recordedHtml = ""
	releaseHtml = ""
	releasedHtml = ""
	row = compositionRow.format(name=nameHtml, descriptions=descriptionsHtml, length=lengthHtml, parts=partsHtml,
		participants=participantsHtml, composed=composedHtml, recorded=recordedHtml, release=releaseHtml, released=releasedHtml)
	return row

def generateComposed(composed):
	start = composed.start
	end = composed.end
	if not composed.start:
		start = "?"
	row = "(" + start + "s";
	if composed.end:
		row += composed.end + "e"
	row += ")"

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
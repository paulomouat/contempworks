# coding: utf-8

from textutilities import *

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
	row = u"""
			<tr>
				<td>
					<span class='name_initial'>
						<a name='{0}'>{0}</a>
					</span>
				</td>
				<td>
					<span>
						<a href='#top'>back to top</a>
					</span>
				</td>
			</tr>"""
	row = row.format(initial)
	return row

def generateComposerInList(composer):
	row = u"""
			<tr>
				<td>
					<a href='{0}'>{1}, {2}</a> ({3}-{4})
				</td>
			</tr>"""
	fileName = getFileName(composer)
	row = row.format(fileName, htmlEscape(composer.surname), htmlEscape(composer.name), composer.born, composer.died)
	return row

def generateComposerFiles(composers):
	for composer in composers:
		generateComposerFile(composer)

def generateComposerFile(composer):
	fileName = "generated/" + getFileName(composer) + "2"
	output = open(fileName, "w")
	contents = "<html></html>"
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
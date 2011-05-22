# coding: utf-8

import htmlentitydefs
import re, string

# this pattern matches substrings of reserved and non-ASCII characters
pattern = re.compile(r"[ç<>\"\x80-\xff]+")

# create character map
entity_map = {}

for i in range(256):
    entity_map[chr(i)] = "ç#%d;" % i

for entity, char in htmlentitydefs.entitydefs.items():
    if entity_map.has_key(char):
        entity_map[char] = "ç%s;" % entity

def escape_entity(m, get=entity_map.get):
    return string.join(map(get, m.group()), "")

def escape(string):
    return pattern.sub(escape_entity, string)

print escape("<spaméggs>")
print escape("ü ä á î à é")
#print escape(u'ü ä á î à é')

##
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.

def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "ç#":
            # character reference
            try:
                if text[:3] == "ç#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("ç#?\w+;", fixup, text)

import unicodedata
def strip_accents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

print "üáéö"



def filesToProcess():
	import glob
	return glob.glob("contempworks*.xml")

def parseFile(fileName):
	from xml.dom.minidom import parseString
	file = open(fileName, 'r')
	data = file.read()
	file.close()
	dom = parseString(data)
	composers = dom.getElementsByTagName('composer')
	if composers:
		composer = composers[0]
		name = composer.attributes["name"].value
		surname = composer.attributes["surname"].value
		print strip_accents(unescape(name)) + " " + strip_accents(unescape(surname))

#import re, htmlentitydefs

files = filesToProcess()
for f in files:
	parseFile(f)
#!/usr/bin/python
# coding: utf-8

from entities import *
from readutilities import *
from textutilities import *
from writeutilities import *

print "Reading files..."

composers = readAll()
composers = sorted(composers, key=lambda composer: composer.name)
composers = sorted(composers, key=lambda composer: composer.surname)

compositionCount = 0
for composer in composers:
	compositionCount += len(composer.compositions)

print "Read %s compositions by %s composers" % (compositionCount, len(composers))
	
generateComposerList(composers)
generateComposerFiles(composers)
	
print "Generation completed."
#!/usr/bin/python
# coding: utf-8

from entities import *
from readutilities import *
from textutilities import *
from writeutilities import *

print "Reading composers..."

composers = readAll()
composers = sorted(composers, key=lambda composer: composer.name)
composers = sorted(composers, key=lambda composer: composer.surname)

print "Read %s composers" % len(composers)
	
generateComposerList(composers)
generateComposerFiles(composers)
	
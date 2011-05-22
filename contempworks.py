# coding: utf-8

from entities import *
from readutilities import *

print "Reading composers..."

composers = readAll()

print "Read %s composers" % len(composers)
	
#for composer in composers:
#	print composer.display()
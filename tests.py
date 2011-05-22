# coding: utf-8

from textutilities import *

test = u"ü á é î ò"
escaped = htmlEscape(test)

print escaped
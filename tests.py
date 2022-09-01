# coding: utf-8

from textutilities import *

test = "ü á é î ò"
escaped = htmlEscape(test)

print(escaped)
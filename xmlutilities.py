# coding: utf-8

from xml.dom import Node

def selectChildren(node, names):
	children = []
	if isinstance(names, (str, unicode)):
		children = [child for child in node.childNodes if child.nodeName == names]
	elif isinstance(names, list):
		children = [child for child in node.childNodes if child.nodeName in names]
	return children

def selectSingleChild(node, name):
	children = selectChildren(node, name)
	if children:
		return children[0]
	return None

def selectSingleChildValue(node, name):
	child = selectSingleChild(node, name)
	value = getTextValue(child)
	return value

def readValue(node, name):
	value = selectSingleChildValue(node, name)
	return value

def getTextValue(node):
	if node:
		textNode = node.firstChild
		if textNode and textNode.nodeType == Node.TEXT_NODE:
			return textNode.nodeValue
	return None

def getAttributeValue(node, name):
	v = None
	if node and node.hasAttribute(name):
		attribute = node.attributes[name]
		v = attribute.value
	return v

def debugNodes(nodes):
	print "outputting %d nodes..." % len(nodes)
	for node in nodes:
		print node
		print "node name = %s, value = %s" % (node.nodeName, node.nodeValue)

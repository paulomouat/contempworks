# coding: utf-8

def selectChildren(node, name):
	children = [child for child in node.childNodes if child.nodeName == name]
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
	
def getTextValue(node):
	if node:
		textNode = node.firstChild
		return textNode.nodeValue
	return None

def getAttributeValue(node, name):
	attribute = node.attributes[name]
	v = attribute.value
	return v

def debugNodes(nodes):
	print "outputting %d nodes..." % len(nodes)
	for node in nodes:
		print node
		print "node name = %s, value = %s" % (node.nodeName, node.nodeValue)

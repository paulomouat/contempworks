class Player(object):
	def __init__(self, name=""):
		self.name = name
	def display(self, indent=""):
		return "%sPlayer name = %s" % (indent, self.name)
			
class Instrument(object):
	def __init__(self, name="", players=None):
		self.name = name
		if players is None:
			players = []
		self.players = players
	def display(self, indent=""):
		output = "%sInstrument name = %s" % (indent, self.name)
		for player in self.players:
			output += "\n" + indent + "  " + player.display("  ")
		return output

class Conductor(object):
	def __init__(self, name=""):
		self.name = name
	def display(self, indent=""):
		return indent + "Conductor name = %s" % self.name

class ComposedPeriod(object):
	def __init__(self, start="", end=""):
		self.start = start
		self.end = end
	def display(self, indent=""):
		return indent + "Composed start = %s, end = %s" % (self.start, self.end)
		
class RecordedPeriod(object):
	def __init__(self, start="", end=""):
		self.start = start
		self.end = end
	def display(self, indent=""):
		return indent + "Recorded start = %s, end = %s" % (self.start, self.end)

class Part(object):
	def __init__(self, number="", name="", length="", description="", composed=None, recorded=None):
		self.number = number
		self.name = name
		self.length = length
		self.description = description
		self.composed = composed
		self.recorded = recorded
	def display(self, indent=""):
		output = "%sPart number = %s" % (indent, self.number)
		output += "\n%s  name = %s" % (indent, self.name)
		output += "\n%s  description = %s" % (indent, self.description)
		output += "\n%s  length = %s" % (indent, self.length)
		output += "\n%s  composed = %s" % (indent, self.composed.display())
		output += "\n%s  recorded = %s" % (indent, self.recorded.display())
		return output
				
class Composition(object):
	def __init__(self, name = ""):
		self.name = name
		self.descriptions = []
		self.length = ""
		self.parts = []
		self.participants = []
		self.composed = ComposedPeriod()
		self.recorded = RecordedPeriod()
		self.release = ""
		self.released = ""
	def display(self, indent=""):
		output = indent + "Composition name = %s" % self.name
		for description in self.descriptions:
			output += "\n" + indent + "  description = %s" % description
		output += "\n" + indent + "  length = %s" % self.length
		for part in self.parts:
			output += "\n" + indent + part.display("  ")
		for participant in self.participants:
			output += "\n" + indent + participant.display("  ")
		output += "\n" + indent + self.composed.display("  ")
		output += "\n" + indent + self.recorded.display("  ")
		output += "\n" + indent + "  release = %s" % self.release
		output += "\n" + indent + "  released = %s" % self.released
		return output

class Composer(object):
	def __init__(self, name="", surname="", born="", died=""):
		self.name = name
		self.surname = surname
		self.born = born
		self.died = died
		self.compositions = []
	def display(self, indent=""):
		output = indent + "Composer name = %s, surname = %s, born = %s, died = %s" % (self.name, self.surname, self.born, self.died)
		for composition in self.compositions:
			output += "\n" + indent + composition.display("  ")
		return output
class Player(object):
	def __init__(self, name=""):
		self.name = name
	def display(self, indent=""):
		return indent + "Player name = " + self.name
			
class Instrument(object):
	def __init__(self, name="", players=None):
		self.name = name
		if players is None:
			players = []
		self.players = players
	def display(self, indent=""):
		output = indent + "Instrument name = " + self.name
		for player in self.players:
			output += "\n" + indent + player.display("  ")
		return output

class ComposedPeriod(object):
	def __init__(self, start="", end=""):
		self.start = start
		self.end = end
	def display(self, indent=""):
		return indent + "Composed start = " + self.start + ", end = " + self.end
		
class RecordedPeriod(object):
	def __init__(self, start="", end=""):
		self.start = start
		self.end = end
	def display(self, indent=""):
		return indent + "Recorded start = " + self.start + ", end = " + self.end

class Part(object):
	def __init__(self, number="", name="", length="", description="", composed=None, recorded=None):
		self.number = number
		self.name = name
		self.length = length
		self.description = description
		self.composed = composed
		self.recorded = recorded
	def display(self, indent=""):
		output = indent + "Part number = " + self.number
		output += "\n" + indent + "  name = " + self.name
		output += "\n" + indent + "  description = " + self.description
		output += "\n" + indent + "  length = " + self.length
		output += "\n" + indent + "  composed = " + self.composed.display()
		output += "\n" + indent + "  recorded = " + self.recorded.display()
		return output
				
class Composition(object):
	def __init__(self, name = ""):
		self.name = name
		self.descriptions = []
		self.length = ""
		self.parts = []
		self.instruments = []
		self.players = []
		self.conductors = []
		self.composed = ComposedPeriod()
		self.recorded = RecordedPeriod()
		self.release = ""
		self.released = ""
	def display(self, indent=""):
		output = indent + "Composition name = " + self.name
		for description in self.descriptions:
			output += "\n" + indent + "  description = " + description
		output += "\n" + indent + "  length = " + self.length
		for part in self.parts:
			output += "\n" + indent + part.display("  ")
		for instrument in self.instruments:
			output += "\n" + indent + instrument.display("  ")
		for player in self.players:
			output += "\n" + indent + player.display("  ")
		for conductor in self.conductors:
			output += "\n" + indent + "  conductor = " + conductor
		output += "\n" + indent + self.composed.display("  ")
		output += "\n" + indent + self.recorded.display("  ")
		output += "\n" + indent + "  release = " + self.release
		output += "\n" + indent + "  released = " + self.released
		return output

class Composer(object):
	def __init__(self, name="", surname="", born="", died=""):
		self.name = name
		self.surname = surname
		self.born = born
		self.died = died
		self.compositions = []
	def display(self, indent=""):
		output = indent + "Composer name = " + self.name + ", surname = " + self.surname
		output += ", born = " + self.born + ", died = " + self.died
		for composition in self.compositions:
			output += "\n" + indent + composition.display("  ")
		return output
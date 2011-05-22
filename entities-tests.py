#!/usr/local/bin/python3.1

# sample code to show version
import entities
inst1 = entities.Instrument("inst1")
inst2 = entities.Instrument("inst2")
pl11 = entities.Player("pl11")
pl12 = entities.Player("pl12")
pl21 = entities.Player("pl21")
pl22 = entities.Player("pl22")
pl23 = entities.Player("pl23")
inst1.players.append(pl11)
inst1.players.append(pl12)
inst2.players.append(pl21)
inst2.players.append(pl22)
inst2.players.append(pl23)

instruments = [inst1, inst2]

for instrument in instruments:
	print instrument.name
	for player in instrument.players:
		print instrument.name + " " + player.name

for instrument in instruments:
	print instrument.display()
		
comp1 = entities.Composer()
comp1.name = "c1n"
comp1.surname = "c1s"
comp1.born = "c11111"
comp1.died = "c12222"

work1 = entities.Composition()
work1.name = "w1"

comp1.compositions.append(work1)

print comp1.display()
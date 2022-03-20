from Person import Person

class Puzzle(object):
	"""
	Knights and Knaves Puzzle class

	Puzzle()
		Constructs a blank Puzzle with no people
	"""

	# Constructs a blank Puzzle with no people
	def __init__(self):
		self.person_list = list()

	def __str__(self):
		ret = ""
		for person in self.person_list:
			ret += str(person) + "\n"
		return ret
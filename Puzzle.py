from Person import Person
from constants import names
import random

class Puzzle(object):
	"""
	Knights and Knaves Puzzle class

	Puzzle()
		Constructs a blank Puzzle with no people
	"""

	# Constructs a blank Puzzle with no people
	def __init__(self):
		self.person_list = list()
		self.solution = ""

	def __str__(self):
		ret = ""
		for person in self.person_list:
			ret += str(person) + "\n"
		return ret

	def solve(self):
		if not self.solution:
			print("Not implemented yet - Puzzle solve()")


# returns a puzzle created from the contents of filename
def make_puzzle_from_file(filename):
	try:
		infile = open(filename, 'r')
	except:
		print("Error in opening {}".format(filename))
		return
	print("Opening file...\n")

	# contents is a list of each line of the puzzle
	contents = infile.read().strip().split("\n")

	# read statements from contents into the Puzzle
	puz = Puzzle()
	for statement in contents:
		# statement is always formed like: [person name] % [logical claim] "[english claim]"
		person_name = statement[ 0 : statement.index(" ") ]
		person_logical_claim = statement[ statement.index("%") + 1 : statement.index("\"") ]
		person_english_claim = statement[ statement.index("\"") + 1 : -1 ]
		# create Person to append
		tmp = Person(person_name)
		tmp.set_logical_claim(person_logical_claim)
		tmp.set_english_claim(person_english_claim)
		# append person to Puzzle's list of people
		puz.person_list.append(tmp)

	# return puzzle object
	return puz

# returns a puzzle created randomly
# number of people and/or knights can be specified and should be -1 for random choice between 2-10 inclusive
def make_random_puzzle():
	# read optional int values, number of people and number of knights,
	# input -1 for random choice
	# if num_knights > num_people, all people are knights
	try:
		num_people = int(input("How many people? "))
		num_knights = int(input("How many knights? "))
		assert (num_knights > 0 or num_knights == -1)
		assert (num_people > 1 or num_people == -1)
	except:
		print("ERROR: Check that number of people is an integer greater than 1 " +
			"and number of knights is a nonnegative integer.")
		return
	
	if (num_people == -1):
		num_people = random.randint(2, 10)
	if (num_knights == -1):
		num_knights = random.randint(2, num_people)

	ret = Puzzle()

	print("num_people: {}".format(num_people))
	print("num_knights: {}".format(num_knights))

	for i in range(0,num_people):
		tmp = Person(names[i])
		tmp.set_status(True) if (i < num_knights) else tmp.set_status(False)
		ret.person_list.append(tmp)
		print(ret.person_list[i])

		

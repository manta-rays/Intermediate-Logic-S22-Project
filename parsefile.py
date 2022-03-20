from Puzzle import Puzzle
from Person import Person

def parse_file(filename):
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
		# append each new person to the Puzzle's list of people
		puz.person_list.append(Person(person_name, person_logical_claim, person_english_claim))

	# return puzzle object
	return puz
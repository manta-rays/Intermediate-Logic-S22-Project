from Puzzle import *

def main():
	##############################################
	# FILE VERSION
	##############################################
	# puzzlefile = input("Name of the Knights and Knaves file: ")
	# fpuzzle = make_puzzle_from_file(puzzlefile)

	# # print the problem before printing the solution
	# print()
	# print("Knights and Knaves - Problem")
	# print(fpuzzle)
	# print()

	# print("Solving...")
	# fpuzzle.solve()

	# print()
	# print("Knights and Knaves - Solution")
	# print(fpuzzle.solution)
	# print()

	##############################################
	# RANDOM VERSION
	##############################################
	print("Knights and Knaves Random Puzzle Generator!")
	rpuzzle = make_random_puzzle()

if __name__ == '__main__':
	main()
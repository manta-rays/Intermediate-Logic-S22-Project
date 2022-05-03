""" Operator nodes """

class IFF(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def print_tree(self, indent_level = 0):
		print(indent_level * ' ' + "IFF")
		self.left.print_tree(indent_level+4)
		self.right.print_tree(indent_level+4)

	def evaluate(self, context):
		return self.left.evaluate(context) == self.right.evaluate(context)

class AND(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def print_tree(self, indent_level = 0):
		print(indent_level * ' ' + "AND")
		self.left.print_tree(indent_level+4)
		self.right.print_tree(indent_level+4)

	def evaluate(self, context):
		return self.left.evaluate(context) and self.right.evaluate(context)

class OR(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def print_tree(self, indent_level = 0):
		print(indent_level * ' ' + "OR")
		self.left.print_tree(indent_level+4)
		self.right.print_tree(indent_level+4)

	def evaluate(self, context):
		return self.left.evaluate(context) or self.right.evaluate(context)

class NOT(object):
	def __init__(self, left):
		self.left = left

	def print_tree(self, indent_level = 0):
		print(indent_level * ' ' + "NOT")
		self.left.print_tree(indent_level+4)

	def evaluate(self, context):
		return not self.left.evaluate(context)

class THEN(object):
	def __init__(self, left, right):
		self.antecedent = left
		self.consequent = right

	def print_tree(self, indent_level = 0):
		print(indent_level * ' ' + "THEN")
		self.antecedent.print_tree(indent_level+4)
		self.consequent.print_tree(indent_level+4)

	def evaluate(self, context):
		return (not self.antecedent.evaluate(context)) or self.consequent.evaluate(context)

class VAR(object):
	def __init__(self, name):
		self.name = name

	def print_tree(self, indent_level = 0):
		print(indent_level * ' ' + '$'+self.name)
		return

	def evaluate(self, context):
		return context[self.name]
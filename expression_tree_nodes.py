""" Operator nodes """

class IFF(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def evaluate(self, context):
		return self.left.evaluate(context) == self.right.evaluate(context)

class AND(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def evaluate(self, context):
		return self.left.evaluate(context) and self.right.evaluate(context)

class OR(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def evaluate(self, context):
		return self.left.evaluate(context) or self.right.evaluate(context)

class NOT(object):
	def __init__(self, left):
		self.left = left

	def evaluate(self, context):
		return not self.left.evaluate(context)

class THEN(object):
	def __init__(self, left, right):
		self.antecedent = left
		self.consequent = right

	def evaluate(self, context):
		return (not self.antecedent.evaluate(context)) or self.consequent.evaluate(context)

class VAR(object):
	def __init__(self, name):
		self.name = name

	def evaluate(self, context):
		return context[self.name]
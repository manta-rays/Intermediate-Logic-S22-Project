class Person(object):
	"""
	Knights and Knaves Person class

	Person()
		Construct a person
	"""
	def __init__(self, name):
		self.name = name
		self.isKnight = None
		self.claim_logic = None
		self.claim_english = None

	def set_logical_claim(self, claim):
		self.claim_logic = claim

	def set_english_claim(self, claim):
		self.claim_english = claim

	def set_status(self, isKnight):
		self.isKnight = isKnight

	def __str__(self):
		return "{}: {}".format(self.name, self.isKnight)
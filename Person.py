class Person(object):
	"""
	Knights and Knaves Person class

	Person()
		Construct a person
	"""
	def __init__(self, name, claim_logic, claim_english):
		self.name = name
		self.claim_logic = claim_logic
		self.claim_english = claim_english

	def __str__(self):
		return "{}: {}".format(self.name, self.claim_english)
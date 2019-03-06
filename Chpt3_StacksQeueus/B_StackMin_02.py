class MinStack():
	def __init__(self):
		self.items, self.minItems = [], []

	def push(value):
		self.items.append(value)

		if not self.minItems or self.minItems[-1] > value:
			self.minItems.append(value)

		return self

	def pop():
		if self.items.isEmpty():
			return None
		else:
			if self.items[-1] is self.minItems[-1]:
				self.minItems.pop()

		return self.items.pop()

	def isEmpty():
		return not self.items

	def peek():
		return self.items[-1]

	def min():
		if not self.minItems:
			return None
		return self.minItems[-1]



class Stack:
	def __init__(self):
		self.items = []

	def __len__(self):
		return len(self.items)

	def isEmpty(self):
		return not self.items

	def pop(self):
		if self.isEmpty():
			return None
		else:
			return self.items.pop()

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self.items[-1]

	def push(self, value):
		self.items.append(value)
		return self

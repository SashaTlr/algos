from random import randint

class Node:
	def __init__(self, value, nextNode = None):
		self.value = value
		self.next = nextNode

	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self, value = None):
		self.head = None
		self.tail = None
		if value is not None:
			self.add(value)

	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __str__(self):
		values = [str(x) for x in self]
		return ' -> '.join(values)


	def add(self, value):
		if self.head is None:
			self.head = self.tail = Node(value)
		else:
			self.tail.next = Node(value)
			self.tail = self.tail.next
		return self

	def addValues(self, values):
		for v in values:
			self.add(v)
		return self

	def generateList(self, n):
		for i in range(n):
			self.add(randint(1, 50))
		return self



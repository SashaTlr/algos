from random import randint

class Node:
	def __init__(self, data):
		self.data = data
		self.size = 1
		self.right = None
		self.left = None

	def insert(self, data):
		if data <= self.data:
			if not self.left:
				self.left = Node(data)
			else:
				self.left.insert(data)
		else:
			if not self.right:
				self.right = Node(data)
			else:
				self.right.insert(data)
		size += 1
		return self

	def find(self, data):
		if data == self.data:
			return self
		return self.__find(data)

	def __find(self, data):
		if data < self.data:
			if self.left:
				return self.left.find(data)
		else:
			if self.right:
				return self.right.find(data)
		return None


	def getIthNode(self, ith):
		if self.size < ith:
			return None
		elif ith == self.size:
			return self
		elif ith < self.left.size:
			self.left.getIthNode(ith - 1)
		else:
			self.right.getIthNode(ith - self.left.size-1)


class BT:
	def __init__(self, data = None):
		self.root = None
		if data:
			self.insert(data)

	def insert(self, data):
		if root:
			root.insert(data)
		else:
			self.root = Node(data)
		return self

	def find(self, node):
		if self.root:
			return self.root.find(data)
		return None

	def delete(self, node):
		self.root = None

	def getRandomNode(self):
		treeRange = self.root.size
		rInt = randint(1, treeRange)
		return self.root.getIthNode(rInt)
		







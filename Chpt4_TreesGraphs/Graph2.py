class Node:

	def __init__(self, value):
		self.value = value
		self.adjacents = []

	def add_adjacent(self, node_adj):
		self.adjacents.append(node_adj)
		return self
		
class BTNode:

	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def add_left(self, left):
		self.left = left
		return self

	def add_right(self, right):
		self.right = right
		return self

	def __str__(self):
		return str(self.value)


class Graph:
	
	def __init__(self):
		self.nodes = []

	def addNode(self, node):
		self.nodes.append(node)
		return self

	def add_edge(self, fromNode, toNode):
		if fromNode not in self.nodes:
			self.addNode(fromNode)

		if toNode not in self.nodes:
			self.addNode(toNode)

		fromNode.add_adjacent(toNode)
		return self


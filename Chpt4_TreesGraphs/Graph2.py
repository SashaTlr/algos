class Node:

	def __init__(self, value):
		self.value = value
		self.adjacents = []

	def add_adjacent(self, node_adj):
		self.adjacents.append(node_adj)
		return self


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


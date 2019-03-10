class Graph:
	def __init__(self):
		self.vertices = {}

	def __iter__(self):
		return iter(self.vertices)

	def __str__(self):
		print(self.vertices)

	def add_node(self, value):
		self.vertices[value] = []
		return self

	def get_node(self, node):
		if node in self.vertices:
			return node
		return None

	def get_nodes(self):
		return self.vertices.keys()

	def add_edge(self, fromNode, toNode):
		if fromNode not in self.vertices:
			add_node(fromNode)

		if toNode not in self.vertices:
			add_node(toNode)

		#undirected
		self.vertices[fromNode].append(toNode)
		self.vertices[toNode].append(fromNode)

		return self


class DirectedGraph:
	def __init__(self):
		self.vertices = {}

	def __iter__(self):
		return iter(self.vertices)

	def __str__(self):
		print(self.vertices)

	def add_node(self, value):
		self.vertices[value] = []
		return self

	def get_node(self, node):
		if node in self.vertices:
			return node
		return None

	def get_nodes(self):
		return self.vertices.keys()

	def add_edge(self, fromNode, toNode):
		if fromNode not in self.vertices:
			add_node(fromNode)

		if toNode not in self.vertices:
			add_node(toNode)

		#undirected
		self.vertices[fromNode].append(toNode)

		return self














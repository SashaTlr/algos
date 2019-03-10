from Graph2 import *
import unittest

def NodeRoute(start, end):

	visited = []

	#find routes between nodes
	if start == end:
		return True

	queue = []

	queue.append(start)

	while queue:

		node = queue.pop()

		for x in node.adjacents:
			if x in visited:
				continue

			if x == end:
				return True

			queue.append(x)

		visited.append(node)

	return False


class Test(unittest.TestCase):
	graph1 = Graph()
	nodes = [Node(x) for x in range(6)]

	graph1.add_edge(nodes[0], nodes[3])
	graph1.add_edge(nodes[0], nodes[4])
	graph1.add_edge(nodes[4], nodes[0])
	graph1.add_edge(nodes[3], nodes[1])
	graph1.add_edge(nodes[3], nodes[2])
	graph1.add_edge(nodes[2], nodes[0])
	graph1.add_edge(nodes[1], nodes[3])
	graph1.add_edge(nodes[5], nodes[3])

	def test_graph(self):
		print(self.assertTrue(NodeRoute(self.nodes[2], self.nodes[1])))
		print(self.assertFalse(NodeRoute(self.nodes[2], self.nodes[5])))

if __name__ == "__main__":
	unittest.main()





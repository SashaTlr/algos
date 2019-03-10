import unittest

class BSTNode:

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

def BinarySearch(array):

	length = len(array)
	
	if length == 0:
		return None

	rootIndex = length / 2
	left_node = BinarySearch(array[:rootIndex])
	right_node = BinarySearch(array[(rootIndex + 1):])

	return BSTNode(array[rootIndex],left_node, right_node)

def printTree(node):
	if node is None:
		return

	printTree(node.left)
	print(node.value)
	printTree(node.right)

class Test(unittest.TestCase):

	bot1 = BinarySearch(range(0))
	bot2 = BinarySearch(range(1))
	bot3 = BinarySearch(range(5))

	def test_BST(self):
		self.assertEqual(self.bot1, None)
		self.assertEqual(self.bot2.value, 0)
		self.assertEqual(self.bot3.value, 2)
		self.assertEqual(self.bot3.left.value, 1)
		self.assertEqual(self.bot3.right.value, 4)
		self.assertEqual(self.bot3.left.left.value, 0)
		self.assertEqual(self.bot3.right.left.value, 3)

if __name__ == "__main__":
	unittest.main()






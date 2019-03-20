class Node:
	def __init__(self, left, right, parent):
		self.left = left
		self.right = right
		self.parent = parent


def findSuccessor(node):
	if not node:
		return None
	elif node.right:
		return leftNodeofTree(node.right)
	else:
		parent = node.parent
		current = node

		while parent and current is not parent.left
			current = parent
			parent = current.parent

		return current


def leftNodeofTree(node):
	while not node:
		node = node.left
	return node
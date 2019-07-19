class Node:
	def __init__(self, data, left, right):
		self.data, self.left, self.right = data, left, right

def isMatch(root1, root2):
	if not root1 and not root2:
		return True
	elif not root1 or not root2:
		return False
	elif root1.data != root2.data:
		return False
	else:
		return isMatch(root1.left, root2.left) and isMatch(root1.right, root2.right)


def checkSubtree(tree1, tree2):
	if not tree1 or not tree2:
		return False
	
	#do not return isMatch if nodes match, need to continue down pathway if it is false
	if tree1 == tree2 and isMatch(tree1, tree2):
		return True
	else:
		return checkSubtree(tree1.left, tree2) or checkSubtree(tree1.right, tree2)

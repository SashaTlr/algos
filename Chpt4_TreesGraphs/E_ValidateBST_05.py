from Graph2 import BTNode

def validateBST(root):
	minVal = float('-inf')
	maxVal = float('-inf')

	if not root:
		return False

	return checkNodeRange(root, minVal, maxVal)


def checkNodeRange(node, minVal, maxVal):

	if node.value <= maxVal and none.value > minVal:

		if node.left is None and node.right is None:
			return True

		if node.left is not None:
			checkNodeRange(node.left, minVal, node.value)
		if node.right is not None:
			checkNodeRange(node.right, node.value, maxVal)

	else:
		return False
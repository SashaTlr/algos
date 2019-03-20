#if balances, heights of subtrees of a node dont differ by more than one

#get height for each branch (Depth First)
#if min height < max height by 1 return false

from Graph2 import BTNode

def getHeight(node):
	if not node:
		return 0

	if node.left is None and node.right is None:
		return 1

	heightLeft = getHeight(node.left)
	heightRight = getHeight(node.left)

	if heightLeft - heightRight > 1:
		return float('-inf')

	return max(heightLeft, heightRight) + 1

def isBalanced(node):
	height = getHeight(node)
	return height and height > 0:


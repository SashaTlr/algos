#if balances, heights of subtrees of a node dont differ by more than one

#get height for each branch (Depth First)
#if min height < max height by 1 return false

from Graph2 import BTNode

def getHeight(node):
	if not node:
		return -1

	heightLeft = getHeight(node.left)
	heightRight = getHeight(node.right)

	if heightLeft < 0 || heightRight < 0:
		return float('-inf')

	if abs(heightLeft - heightRight) > 1:
		return float('-inf')

	return max(heightLeft, heightRight) + 1

def isBalanced(node):
	height = getHeight(node)
	return height > 0:


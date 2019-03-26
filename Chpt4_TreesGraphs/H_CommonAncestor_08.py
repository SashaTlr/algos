class Node:
	def __init__(self, value, left, right):
		self.value, self.left, self.right = value, left, right


class Result:
	def __init__(self, isAncestor, node):
		self.isAncestor = isAncestor
		self.node = node

def LCA(p, q, root):

	if not root:
		return None

	if p is q:
		return p;

	result = commonAncestor(p, q, root)

	if result.isAncestor:
		return node
	
	return None

def commonAncestor(p, q, root):
	#case if q is a descendant of p
	#case p or q are not in tree
	#case p is in subtree and q not in subtree
	#case p and q in same subtree

	if not root:
		return Result(false, None)

	if root is q && root is p:
		return Result(True, root)

	nodeX = commonAncestor(root.left, p, q)
	if nodeX.isAncestor:
		return nodeX

	nodeY = commonAncestor(root.right, p, q)
	if nodeY.isAncestor:
		return nodeY


	if nodeX.node and nodeY.node:
		return Result(true, root)

	#if root is equal to one of the nodes, that root hasn't been visited yet
	#if one of the results also contains a node, that means the root is also 
	#ancestor to the other node so set flag to true
	elif root is q or root is p:
		isAncestor = not nodeX.node or not nodeY.node
		return Result(isAncestor, root)

	else:
		#found node, passing it up the chain to parent node
		return Result(false, nodeX.node if nodeX.node else nodeY.node)

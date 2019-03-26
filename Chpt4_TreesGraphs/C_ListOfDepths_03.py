#breadth search

#on call for each level, pass back node #
#find node # key in list, add node to linked list 
#we're going to use arrays instead of LL :)
class BTNode:

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



def ListofDepthsBFS(root):
	resultList = []
	#use current list to iterate first depth
	#switch to parrent to traverse next list
	if not root:
		return None

	currentList = [root]

	while len(currentList) > 0:
		resultList.append(currentList)
		parentList = currentList
		currentList = []

		for node in parentList:

			if node.left:
				currentList.append(node.left)
			if node.right:
				currentList.append(node.right)


	return resultList


def ListOfDepthsDFS(root):
	ll = [[]]
	ListofDepthsDFSRecursion(root, ll, 0)
	return ll

def ListofDepthsDFSRecursion(root, ll, level = 0):
	if not root:
		return

	if len(ll) < level + 1:
		ll.append([])

	ll[level].append(root)

	ListofDepthsDFS(root.left, ll, level + 1)
	ListofDepthsDFS(root.right, ll, level + 1)

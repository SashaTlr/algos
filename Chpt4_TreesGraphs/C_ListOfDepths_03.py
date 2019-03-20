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
	currentList = []

	if not root:
		return None

	currentList.append(root)

	while len(currentList) > 0:
		
		result.append(currentList)
		parentList = currentList
		currentList = []

		for node in parentList:
			if node.left is not None:
				currentList.append(node.left)
			if node.right is not None:
				currentList.append(node.right)

	return resultList

def ListofDepthsDFS(root, level = 0, ll = [[]]):
	if not root:
		return ll

	if len(ll) <= level:
		ll.append([])

	ll[level].append(root)

	ListofDepthsDFS(root.left, level + 1, ll)
	ListofDepthsDFS(root.right, level + 1, ll)


# result = array of linked lists of nodes
#initialize new list
#if root isnlt null, add root to new list

#while current list isnt 0, add current to result

#create parent list and set equal to current list
#current is new list
#for loop through nodes in parent list
#add non null children of parent list to current
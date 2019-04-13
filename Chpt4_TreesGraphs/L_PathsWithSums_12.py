#pathswithsum

#depth first search
#create hash for every node step
class Node:
	def __init__(self, data, left = None, right = None):
		self.data, self.left, self.right = data, left, right


def PathsWithSums(root, targetSum):
	if root:
		stack.append(root)
		return PathsWithSumsRecurse(targetSum, stack)
	return None

def PathsWithSumsRecurse(node, targetSum, curr_sum = 0, hashSum= =  {0: 1}):
	if not node:
		return 0

	curr_sum += node.data

	if curr_sum not in hashSum:
		hashSum[curr_sum] = 1
	else:
		hashSum += 1

	if curr_sum - targetSum in hashSum:
		count += hashSum[curr_sum - targetSum]

	count += PathsWithSumsRecurse(node, targetSum, curr_sum, hashSum)
	count += PathsWithSumsRecurse(node, targetSum, curr_sum, hashSum)

	hashSum[curr_sum] -= 1

	return count


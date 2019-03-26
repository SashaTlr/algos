#new options has all options minus the one inspected
#new options include subnodes of inspected option
#inspected node will be added to partial, so options will always be after this
class Node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

def bst_sequences(node):
	return bst_sequences_helper([], [node])

#must preserve order in each result sequence when weaving
#by adding node's children to subtree after adding subtree node
#to results, order is guaranteed

def bst_sequences_helper(permutations, subtrees):
	#base case
	#when no more nodes, return results. It is a double array, so cumulatively adding
	#sequences builds a list of arrays, it doesn't append to single array

	if len(subtrees) == 0:
		return [permutations]

	#for first node, want to return bst_sequences_helper([node1], [child1, child2])
	#ENUMERATE returns index AND value

	sequences = []
	for index, subtree in enumerate(subtrees):
		new_perms = permutations + [subtree.data]

		#exclude moved subtree node from new subtree array
		new_subtrees = [:index] + [index + 1:]

		#add children of subtree to new subtree
		#will always be left of parent
		#order will be swapped next iteration

		if subtree.left:
			new_subtrees += subtree.left

		if subtree.right:
			new_subtrees += subtree.right

	#builds until no subtrees left, returns list of permutations
	sequences += bst_sequences_helper(new_perms, new_subtrees)
	return sequences

	





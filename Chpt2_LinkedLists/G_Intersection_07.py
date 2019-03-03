from LinkedList import LinkedList
from LinkedList import Node
import unittest

def ListIntersection(ll_one, ll_two):
	length_two = length_one = 0

	if ll_one.tail != ll_two.tail:
		return None

	for x in ll_one:
		length_one += 1

	for y in ll_two:
		length_two += 1

	ll_diff = abs(length_two - length_one)

	if length_one >= length_two:
		pointer1, pointer2 = ll_one.head, ll_two.head
	else:
		pointer1, pointer2 = ll_two.head, ll_one.head

	for i in range(ll_diff):
		pointer1 = pointer1.next

	while pointer1 is not pointer2:
		pointer1, pointer2 = pointer1.next, pointer2.next

	return pointer1

class Test(unittest.TestCase):

	node = Node(3, None)
	node_two = Node(5, node)
	node_three = Node(6, node_two)

	test_data = [(
		LinkedList(), 
		LinkedList().generateList(3).addNode(node_three), None), (
		LinkedList().generateList(3).addNode(node_three), 
		LinkedList().generateList(3).addNode(node_three), node_three)]

	def test_ListIntersection(self):
		for [list_one, list_two, expected] in self.test_data:
			actual = ListIntersection(list_one, list_two)
			self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()





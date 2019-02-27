from LinkedList import LinkedList
import unittest

def delete_middle_node(node):

	if node is None or node.next is None:
		return

	node.value = node.next.value
	node.next = node.next.next


class Test(unittest.TestCase):

	test_list = LinkedList().addValues([1,2,3,4,5])
	expected_list = LinkedList().addValues([1,2,4,5])
	node = test_list.getNode(2)

	test_data = [(test_list, expected_list, node)]

	def test_delete_middle_node(self):
		for [test_list, expected_list, node] in self.test_data:
			actual = delete_middle_node(node)
			self.assertEqual(str(test_list), str(expected_list))

if __name__ == "__main__":
	unittest.main()
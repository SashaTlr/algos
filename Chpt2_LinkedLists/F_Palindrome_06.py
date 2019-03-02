from LinkedList import LinkedList
import unittest

class Result():

	def __init__(self, node, isPal):
		self.node = node
		self.isPal = isPal


def get_list_size(node):
	size = 0

	while node:
		size += 1
		node = node.next

	return size

def isPalindrome(ll):
	length = get_list_size(ll.head)
	res = IsPalindromeRecursive(ll.head, length)
	return res.isPal

def IsPalindromeRecursive(head, length):
	if length <= 0 or head is None:
		return Result(head, True)
	elif length == 1:
		return Result(head.next, True)

	res = IsPalindromeRecursive(head.next, length - 2)

	if res.isPal is False or res.node is None:
		return res

	res.isPal = res.node.value == head.value
	res.node = res.node.next

	return res;

class Test(unittest.TestCase):
	
	test_data = ([LinkedList().addValues(['a','b', 'b', 'a']), True], [LinkedList().addValues(['a','b', 'a']), True], 
		[LinkedList().addValues(['a', 'b', 'c', 'a']), False])

	def test_IsPalindrome(self):
		for [data, expected] in self.test_data:
			actual = isPalindrome(data)
			print(actual)
			self.assertEqual(expected, actual)


if __name__ == "__main__":
	unittest.main()









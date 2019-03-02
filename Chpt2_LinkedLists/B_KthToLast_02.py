from LinkedList import LinkedList
import unittest

def kthLast(ll, k):
	pointer = ll.head
	kthLastPointer = ll.head

	if pointer is None:
		raise ValueError("Linked list is empty")

	for i in range(k):
		if pointer.next is None:
			raise ValueError("Linked list is shorter than k-th value")
		pointer = pointer.next

	while pointer:
		kthLastPointer = kthLastPointer.next
		pointer = pointer.next

	return kthLastPointer


class TestCase(unittest.TestCase):

	testData = [(LinkedList().addValues([1,2,3,4,5,6,7,8,9,10]), 3, 8)]

	def test_kthLast(self):
		for [test, k, expected] in self.testData:
			actual = kthLast(test, k)
			self.assertEqual(str(actual), str(expected))

if __name__ == "__main__":
	unittest.main()


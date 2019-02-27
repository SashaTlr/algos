from LinkedList import LinkedList
import unittest

def RemoveDups(ll):

	tracker = set([ll.head.value])

	current =ll.head

	while current.next:
		if current.next.value in tracker:
			current.next = current.next.next
		else:
			tracker.add(current.next.value)
			current = current.next

	return ll

#Using no buffer

def RemoveDupsNoBuffer(ll):

	pointer = ll.head
	dupCheckPointer = pointer
	
	while pointer:
		while dupCheckPointer.next:
			if dupCheckPointer.next.value == pointer.value:
				dupCheckPointer.next = dupCheckPointer.next.next
				dupCheckPointer = dupCheckPointer.next

		pointer = pointer.next

	return ll


class Test(unittest.TestCase):

	expectedList = LinkedList().addValues([1,2,3,4,5])
	testList = LinkedList().addValues([1,2,3,3,4,3,4,5,4])

	def test_RemoveDups(self):
		actualWithBuffer = RemoveDups(self.testList)
		actual = RemoveDups(self.testList)

		self.assertEqual(str(self.expectedList), str(actualWithBuffer))
		self.assertEqual(str(self.expectedList), str(actual))

if __name__ == "__main__":
	unittest.main()
	
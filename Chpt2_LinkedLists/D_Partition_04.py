
from LinkedList import LinkedList 
import unittest

def PartitionList(ll, partitionValue):
	head = ll.head
	tail = ll.head

	currentNode = ll.head

	while currentNode:
		nextNode = currentNode.next
		if currentNode.value < partitionValue:
			currentNode.next = head
			head = currentNode
		else:
			tail.next = currentNode
			tail = currentNode
	
		currentNode = nextNode

	ll.head = head
	tail.next = None

	return ll

class Test(unittest.TestCase):
	inputList = LinkedList().addValues([1 , 23 , 46 , 34 , 9 , 18 , 21 , 33 , 18 , 11])
	expectedList = LinkedList().addValues([11 , 18 , 18 , 9 , 1 , 23 , 46 , 34 , 21 , 33])

	test_data = [(inputList, 20, expectedList)]

	def test_PartitionList(self):
		for [inputList, partitionValue, expectedList] in self.test_data:
			actualList = PartitionList(inputList, partitionValue)

			self.assertEqual(str(actualList), str(expectedList))


if __name__ == "__main__":
	unittest.main()
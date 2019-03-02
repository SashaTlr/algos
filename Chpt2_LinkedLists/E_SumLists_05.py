from LinkedList import LinkedList
import unittest

def SumLists(ll_one, ll_two):

	carryover = 0
	pointer = ll_one.head
	pointer2 = ll_two.head

	sumList = LinkedList()

	while pointer or pointer2 or carryover > 0:
		sumValue = carryover

		if pointer:
			sumValue += pointer.value
			pointer = pointer.next

		if pointer2:
			sumValue += pointer2.value
			pointer2 = pointer2.next
		
		sumList.add(sumValue % 10)

		carryover = sumValue / 10

	return sumList

	
class Test(unittest.TestCase):
	data = [(LinkedList().addValues([6,1,8]), LinkedList().addValues([9,1,2]), LinkedList().addValues([5, 3, 0 , 1]))]

	def test_SumLists(self):
		for [ll_one, ll_two, expected] in self.data:
			actual = SumLists(ll_one, ll_two)

		self.assertEqual(str(actual), str(expected))

if __name__ == "__main__":
	unittest.main()
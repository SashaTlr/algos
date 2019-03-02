from LinkedList import LinkedList

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
		
		sumList.addNode(sumValue % 10)

		carryover = sumList / 10

	return sumList

	
	


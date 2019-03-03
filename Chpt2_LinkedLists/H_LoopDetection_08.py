from LinkedList import LinkedList, Node
import unittest
from random import randint

def LoopDetection(ll):

	slow = fast = ll.head

	#start at same point so can't check slow and fast comparison at beginning of while condition 
	#(will end at first check)
	
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			break	

	fast = ll.head

	while slow != fast:
		slow = slow.next
		fast = fast.next

	return fast





class Test(unittest.TestCase):
	ll_one = LinkedList().generateList(20)
	loop_one = ll_one.head.next.next.next.next.next
	ll_one.tail.next = loop_one

	ll_two = LinkedList().generateList(20)
	loop_two = ll_two.head.next.next.next.next
	ll_two.tail.next = loop_two

	ll_three = LinkedList()

	ll_four = LinkedList().generateList(1)

	test_data = ([ll_one, loop_one], [ll_two, loop_two], [ll_three, None], [ll_four, None])

	def test_loop_detection(self):
		
		for [ll, expected] in self.test_data:
			actual = LoopDetection(self.ll_one)
			self.assertEqual(actual, self.loop_one)

if __name__=="__main__":
	unittest.main()















from Stack import Stack

def sortStack(stack):

	temp_stack = Stack()

	temp_stack.push(stack.pop())

	#pop an element off and hold in a variable
	#peek at element in temp_stack
	#if greater, just push on top
	#if less, keep popping until you reach smaller element (use peek)
	#insert temp element
	#push rest back on

	while not stack.isEmpty():
		value = stack.pop()

		while temp_stack.peek() > value or not temp_stack.isEmpty():
			stack.push(temp_stack.pop())
		temp_stack.push(value)

	while not temp_stack.isEmpty():
		stack.push(temp_stack.pop())

	return stack

class Test(unittest.TestCase):
	stack = Stack()
	stack.push(4).push(3).push(5).push(8).push(1)

	sorted_stack = sortStack(stack)

	self.assertEqual(sorted_stack.pop(), 1)
	self.assertEqual(sorted_stack.pop(), 3)
	self.assertEqual(sorted_stack.pop(), 4)
	self.assertEqual(sorted_stack.pop(), 5)
	self.assertEqual(sorted_stack.pop(), 8)

if __name__ == "__main__":
	unittest.main()
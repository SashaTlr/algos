from Stack import Stack
import unittest

class MyQueue:
	def __init__(self):
		self.pop_stack = Stack()
		self.push_stack = Stack()

	def push(self, value):
		while not self.pop_stack.isEmpty():
			self.push_stack.push(self.pop_stack.pop())

		self.push_stack.push(value)

		while not self.push_stack.isEmpty():
			self.pop_stack.push(self.push_stack.pop())

		return self;

	def pop(self):
		return self.pop_stack.pop()
		
	def peek(self):
		return self.pop_stack.peek()

	def isEmpty(self):
		return self.pop_stack.isEmpty()


class Test(unittest.TestCase):
	def test_MyQueue(self):
		stack = MyQueue()
		
		self.assertTrue(stack.isEmpty())

		stack.push(4)
		self.assertFalse(stack.isEmpty())
		self.assertEqual(stack.pop(), 4)
		self.assertTrue(stack.isEmpty())

		stack.push(3)
		stack.push(4)
		stack.push(5)

		self.assertFalse(stack.isEmpty())

		self.assertEqual(stack.pop(), 3)
		self.assertEqual(stack.pop(), 4)
		self.assertEqual(stack.pop(), 5)

		self.assertTrue(stack.isEmpty())

if __name__ == "__main__":
	unittest.main()

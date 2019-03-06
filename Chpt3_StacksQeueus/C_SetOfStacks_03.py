from Stack import Stack
import unittest

class SetOfStacks:

	def __init__(self, capacity = 5):
		self.stackCapacity = capacity
		self.sets = []

	def push(self, value):
		if self.isEmpty() or self.__stackAtCapacity(self.sets[-1]):
			self.sets.append(Stack().push(value))
		else:
			self.sets[-1].push(value)
		return self

	def pop(self):
		if self.isEmpty():
			return None
		else:
			popped = self.sets[-1].pop()
			
			#delete empty stack if empty
			if self.sets[-1].isEmpty():
				self.sets.pop()

		return popped


	def isEmpty(self):
		return not self.sets

	def __stackAtCapacity(self, stack):
		len(stack) == self.stackCapacity


class Test(unittest.TestCase):
	
	def test_SetOfStacks(self):
		stacks = SetOfStacks(3)
		stacks.push(5)
		self.assertEqual(5, stacks.pop())
		self.assertEqual(True, stacks.isEmpty())
		stacks.push(5)
		stacks.push(6)
		stacks.push(7)
		stacks.push(8)
		self.assertEqual(8, stacks.pop())
		self.assertFalse(stacks.isEmpty())


if __name__ == "__main__":
	unittest.main()

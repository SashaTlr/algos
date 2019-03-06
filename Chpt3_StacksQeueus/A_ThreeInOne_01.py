
class Multistack:

	def __init__(self, stackOne, stackTwo, stackThree):
		self.topStack = [stackOne, stackTwo, stackThree]
		self.array = [None] * (stackOne.capacity + stackTwo.capacity + stackThree.capacity)

	class StackInfo:
		def __init__(topIndex, capacity = 10):
			self.top = topIndex
			self.size = 0
			self.capacity = capacity

			return self

		def isFull(self):
			return self.size >= self.capacity

		def isEmpty(self):
			return self.size == 0


		def _getIndex(self):
			if (self.size + self.top - 1) > len(self.array):
				return (self.size + self.top) % len(self.array)
			
			return self.size + self.top



	def push(self, value, stackNum):
		if __allStacksAreFull():
			raise Exception ("All stacks are full")

		stack = self.topStack[stackNum]

		if stack.isFull():
			__expandStack(stackNum)

		index = stack._getIndex()

		self.array[index] = value
		stack.size += 1

		return self

	def pop(self, stackNum):
		
		stack = self.topStack[stackNum]

		if stack.isEmpty():
			return None

		popped_value = self.array[stack._getIndex()]
		self.array[stack._getIndex()] = None

		stack.size -= 1

	def peek(self, stackNum):
		stack = self.topStack[stackNum]

		if stack.isEmpty():
			return None

		popped_value = self.array[_getIndex(stack)]

		stack.size -= 1

	def __allStacksAreFull():
		#are all stacks full

	def __expandStack(stackNum):
		#needs to expand stack 
		#if no room, has to shift other stacks, expand capacity


#Need to use space efficiently
#have an array that tracks beginning of each stack
#have a method that checks if next space is available. if not, call shift method
#shift method must check for availability of next space before shifting
#shift method - if you reach the end, can wrap around if beginning is empty
#topstack contains size of stack, first position
#if size + first position index is greater than length of array, there is an overflow






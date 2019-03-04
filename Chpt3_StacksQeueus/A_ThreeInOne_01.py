class StackInfo:
	def __init__(topIndex, capacity = 10):
		self.top = topIndex
		self.size = 0
		self.capacity = capacity

		return self

	def isFull(self):
		if self.size > self.capacity:
			return False:
		return True;

	def isEmpty(self):
		if self.size == 0:
			return True
		return False


class Multistack:

	def __init__(self, stackOne, stackTwo, stackThree):
		self.topStack = [stackOne, stackTwo, stackThree]
		self.array = [None] * (stackOne.capacity + stackTwo.capacity + stackThree.capacity)


	def push(self, value, stackNum):
		if __allStacksAreFull():
			raise Exception ("All stacks are full")

		stack = topStack[stackNum]

		if stack.isFull():
			__expandStack(stackNum)

		index = stack.top + 1
		self.array[index] = value
		stack.size += 1

		#doesn't account for wrapping: need to adjust index to wrap around beginning of array

		return self

	def __allStacksAreFull():
		#are all stacks full

	def __expandStack(stackNum):
		#needs to expand stack 
		#if no room, has to shift other stacks, expand capacity

	def pop(self, stackNum):
		
		stack = self.topStack[stackNum]

		if stack.isEmpty():
			return None

		#doesn't deal with wraparound index
		popped_value = self.array[stack.top + size]


	def _getIndex(stackNum):
		if stackNum.size + stackNum.top > len(self.array):
			return (stackNum.size + stackNum.top) % len(self.array)
		
		return stackNum.size + stackNum.top

#Need to use space efficiently
#have an array that tracks beginning of each stack
#have a method that checks if next space is available. if not, call shift method
#shift method must check for availability of next space before shifting
#shift method - if you reach the end, can wrap around if beginning is empty
#topstack contains size of stack, first position
#if size + first position index is greater than length of array, there is an overflow
#to delete an element, if it is the top element, the top needs to move
#if not top element, shift elements right to close gap






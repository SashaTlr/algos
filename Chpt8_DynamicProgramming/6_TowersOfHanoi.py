class Tower:
	def __init__(self):
		self.items = []

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) is 0

	def push(self, item):
		self.items.append(item)
		return self

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self.items[-1]

	def move_disk(self, destTower):
		if not self.isEmpty():
			if self.peek() <= destTower.peek():
				destTower.push(self.pop())
			else:
				raise Exception("disk is too large")
		return destTower


def TowersOfHanoi(initTower, bufferTower, destTower):
	if len(initTower) == 1:
		initTower.move_disk(destTower)
		return (initTower, bufferTower, destTower)

	if len(initTower) == 2:
		initTower.move_disk(bufferTower):
		initTower.move_disk(destTower)
		bufferTower.move_disk(destTower)
		return (initTower, bufferTower, destTower)

	if len(initTower == 3)
		initTower, bufferTower, destTower = TowersOfHanoi(initTower[:2], destTower, bufferTower)
		initTower.move_disk(destTower)
		return TowersOfHanoi(initTower, bufferTower, destTower)






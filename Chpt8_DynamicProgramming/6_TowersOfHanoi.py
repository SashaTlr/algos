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

	def move_top_disk(self, destTower):
		if not self.isEmpty():
			if self.peek() <= destTower.peek():
				destTower.push(self.pop())
			else:
				raise Exception("disk is too large")
		return destTower

	def move_disks(self, n, destination, buffers):
		if n > 0:
			self.move_disks(n-1, buffers, destination) #move n-1 to buffer tower
			self.move_top_disk(destination) #when n = 1
			buffers.(n-1, destination, self)
			#move n-1 disks to destination via buffer

Start = new Tower.push(1).push(2).push(3).push(4)
Buffer = new Tower()
Dest = new Tower()

Start.move_disks(4, Dest, Buffer)
		Start.move_disks(3, Buffer, Dest)
			Start.move_disks(2, Dest, Buffer)
				Start.move_disks(1, Buffer, Dest)
					Start.move_top_disk(Buffer)
				Buffer.move_disks(1, Dest, Start)
			








import unittest

def FlipBit(num):

	if num == 0:
		return 0

	if num == -1:
		return 64

	current_count = 0
	prev_count = 0
	max_count = 0

	bit = 1

	while num != 0:

		#if last digit is a 1
		if num & 1 == 1:
			current_count += 1
		elif num == -1:
			current_count += 1
			num == 0
		else:
			max_count = max(max_count, prev_count + current_count)
			prev_count = current_count
			current_count = 0

		num >>= 1

	max_count = max(max_count, prev_count + current_count)

	return max_count

class Test(unittest.TestCase):

	def test_FlipBit(self):
		self.assertEqual(FlipBit(-1), 64)
		self.assertEqual(FlipBit(31934353297), 7)
		self.assertEqual(FlipBit(0), 0)
		self.assertEqual(FlipBit(52), 3)

if __name__ == "__main__":
	unittest.main()
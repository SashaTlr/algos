def recurse_multiple(pos1, pos2):
	side1 = max(pos1, pos2)
	side2 = min(pos1, pos2)

	return recurse_multiple_helper(side2, side1)

def recurse_multiple_helper(smaller, bigger):
	if smaller == 0:
		return 0

	if smaller == 1:
		return bigger

	half = smaller >> 1
	halfproduct = recurse_multiple_helper(half, bigger)

	if smaller % 2 == 0:
		return (halfproduct << 1)
	else:
		return (halfproduct << 1) + bigger

import unittest
class TestCase(unittest.TestCase):
	def test_recurse_multiple(self):
		self.assertEqual(recurse_multiple(1, 12), 12)
		self.assertEqual(recurse_multiple(1, 9), 9)
		self.assertEqual(recurse_multiple(6, 20), 120)
		self.assertEqual(recurse_multiple(6, 21), 126)
		self.assertEqual(recurse_multiple(0, 13), 0)
		self.assertEqual(recurse_multiple(9, 9), 81)

if __name__=="__main__":
	unittest.main()
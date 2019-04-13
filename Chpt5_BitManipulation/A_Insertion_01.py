import unittest

def insertion(N, M, i, j):
	mask = (~0b0 << (j+1)) | ((0b1 << i) - 1) 
	return N & mask | M << i


class Test(unittest.TestCase):
	def test_insertion(self):
		self.assertEqual(insertion(0b10000000000, 0b10011, 2, 6), 0b10001001100)
		self.assertEqual(insertion(0b11111111111, 0b10010, 2, 6), 0b11111001011)


if __name__ == "__main__":
	unittest.main()

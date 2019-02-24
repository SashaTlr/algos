import unittest

def rotate(arr):

	N = len(arr)
	M = len(arr[0])

	if M != N:
		raise ValueError("Input array is not a square")

	for col in range(N/2):
		last = N - col - 1
		for row in range(col, last):
			offset = row - col
			arr[col][row], arr[last - offset][col], arr[last][last-offset], arr[row][last] = arr[last - offset][col], arr[last][last-offset], arr[row][last], arr[col][row]

	return arr;


class Test(unittest.TestCase):
	"""docstring for Test"""
	test = [ ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])]

	def test_rotate_matrix(self):
		for [testdata, expectation] in self.test:
			result = rotate(testdata)
			self.assertEqual(expectation, result)

if __name__ == "__main__":
	unittest.main()
import unittest

def zero_matrix(arr):

	if len(arr) == 0 or isinstance(arr[0], int):
		raise ValueError("Not a 2D matrix")

	for i in range(len(arr)):
		firstColHasZeros = False
		if arr[i][0] == 0:
			firstColHasZeros = True
			break

	for i in range(len(arr[0])):
		firstRowHasZeros = False
		if arr[0][i] == 0:
			firstRowHasZeros = True
			break

	for i in range(1, len(arr)):
		for j in range(1,len(arr[0])):
			if arr[i][j] == 0:
				arr[i][0] = 0
				arr[0][j] = 0


	for i in range(len(arr)):
		if arr[i][0] == 0:
			SetRowToZeros(arr, i)

	for i in range(len(arr[0])):
		if arr[0][i] == 0:
			SetColToZeros(arr, i)

	if firstRowHasZeros:
		SetRowToZeros(arr, 0)

	if firstColHasZeros:
		SetColToZeros(arr, 0)

	return arr
	
def SetColToZeros(arr, colIndex):
	for i in range(len(arr[colIndex])):
		arr[i][colIndex] = 0


def SetRowToZeros(arr, rowIndex):
	for i in range(len(arr)):
		arr[rowIndex][i] = 0

class Test(unittest.TestCase):
	data = [([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ],[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])]

	def test_zero_matrix(self):
		for [test, expected] in self.data:
			actual = zero_matrix(test)
			self.assertEqual(expected, actual)


if __name__ == "__main__":
	unittest.main()


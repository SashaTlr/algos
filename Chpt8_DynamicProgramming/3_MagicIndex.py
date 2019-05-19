def magic_index(arr):
	mid = len(arr)/2
	start = 0
	end = len(arr)

	while start <= end:
		if arr[mid] == mid:
			return mid
		elif arr[mid] > mid:
			end = mid
			mid = (start + end) / 2
		else:
			start = mid
			mid = (start + end)/2

	if arr[mid] == mid: return mid

	return None


def magic_index_dupes(arr):
	start = 0
	end = len(arr) - 1 
	return magic_index_dupes_recurse(arr, start, end)

def magic_index_dupes_recurse(arr, start, end):
	if end < start:
		return -1

	mid = (start+ end)/2
	midVal = arr[mid]

	if midVal == mid:
		return mid

	leftIndex = min(mid-1, midVal)
	left = magic_index_dupes_recurse(arr, start, leftIndex)
	if left >= 0:
		return left

	rightIndex = max(mid+1, midVal)
	right = magic_index_dupes_recurse(arr, rightIndex, end)
	return right

import unittest
class TestClass(unittest.TestCase):
	arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
	arr1 = [-10, -5, 2, 2, 2, 3, 4, 8,9, 12, 13]

	def test_magic_index(self):
		self.assertEqual(magic_index(self.arr), 7)
		self.assertEqual(magic_index_dupes(self.arr1), 2)

if __name__ == "__main__":
	unittest.main()

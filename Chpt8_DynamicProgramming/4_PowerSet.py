def power_set(full_set):
	
	for i in range(len(full_set)):
		item = full_set[i]
		if i is 0:
			dp_curr = [[item]]
		else:
			dp_curr.append([item])
			for subset in dp_prev:
				temp = subset[:]
				temp.append(item)
				dp_curr.append(temp[:])

		dp_prev = dp_curr[:]

	dp_curr.append([])
	return dp_curr

def power_set_binary(full_set):
	subset_size = 1 << len(full_set)
	full_subset = []
	for item in range(subset_size):
		full_subset.append(_convertToSet(item, full_set))

	return full_subset

def _convertToSet(item, full_set):
	index = 0
	subset = []

	while item > 0:
		if item & 1 is 1:
			subset.append(full_set[index])

		item >>= 1
		index += 1

	return subset

import unittest
class TestCase(unittest.TestCase):
	fullset = [1, 2, 3]
	expected = [ [], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1,2,3]]

	def test_power_subset(self):
		self.assertEqual(len(power_set(self.fullset)), len(self.expected))
		self.assertEqual(len(power_set_binary(self.fullset)), len(self.expected))

if __name__ == "__main__":
	unittest.main()




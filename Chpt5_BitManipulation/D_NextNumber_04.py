def getNext(num):

	if num == 0:
		return None

	#copy num
	c = num
	c0, c1 = 0, 0
	#get trailing zero count
	while (c & 1 == 0) and c != 0 and c0 <= 32:
		c0 += 1
		c >>= 1

	#get 1s block
	while (c & 1 == 1) and c1 <= 32:
		c1 += 1
		c >>= 1

	#adding 2^c0s + 1 will set element at p (c0 + c1) to 1 and rest to 0
	#e.g. 11001111000 + (2^c0) + 1 = 11001111000 + (2^3 - 1) + 1 --> 
	# 1001111000 + 1000 - 1 + 1 --> 11001111000 + 111 + 1 --> 11001111111 + 1 = 11010000000
	# simplifies to num + 2^c0
	# add in c1 - 1 1s
	# --> + 2^c1-1 - 1 (eg c1 = 3 --> 1 << 2 --> 100 --> 100 - 1 --> 011)

	# num + 2^c0s + 2^c1-1 - 1

	if c0 + c1 == 0:
		nextNum = None
	else:
		nextNum = num + (1 << c0) + (1 << (c1 - 1)) - 1
	
	c = num
	c0, c1 = 0, 0
	#get trailing zero count
	while ((c & 1) == 1) and c1 <= 32:
		c1 += 1
		c >>= 1

	#get 1s block
	while (c &  1 == 0 ) and c != 0 and c0 <= 32:
		c0 += 1
		c >>= 1

	#removing 2^c1 - 1 removes trailing 1s
	#minus 1 flips trailing 0s to 1 and flips first 1 in block to 0
	#minusing c0 -1 1's adds 0s back in as trailing 0s
	#becomes num - (2^c1 - 1) - 1 - (2^c0-1 - 1)

	if c0 + c1 == 0:
		prevNum = None
	else:
		prevNum = num - (1 << c1) - (1<< (max(0, c0 - 1))) + 1
	
	return (prevNum, nextNum)


import unittest

class Test(unittest.TestCase):
  def test_next_numbers(self):
    self.assertEqual(getNext(8), (4, 16))
    self.assertEqual(getNext(12), (10, 17))
    self.assertEqual(getNext(15), (-1, 23))
    self.assertEqual(getNext(143), (124, 151))
    self.assertEqual(getNext(159), (126, 175))

if __name__ == "__main__":
  unittest.main()


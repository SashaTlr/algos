import unittest

def binaryToString(num):

	binaryNum = 1/2.0
	divisor = 2.0
	binaryStr = "0."

	if num < 0 or num > 1:
		return "ERROR"

	while len(binaryStr) <= 33:
		if (num - binaryNum) > 0:
			binaryStr += "1"
			num -= binaryNum

		elif (num - binaryNum) < 0:	
			binaryStr += "0"

		elif num == binaryNum:
			binaryStr += "1"
			return binaryStr

		binaryNum /= divisor

	return "ERROR"

class Test(unittest.TestCase):

	def test_binaryToStr(self):
		self.assertEqual(binaryToString(0.50), "0.1")
		self.assertEqual(binaryToString(0.625), "0.101")
		self.assertEqual(binaryToString(0.3), "ERROR")

if __name__ == "__main__":
	unittest.main()
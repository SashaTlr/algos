def TripleStep(numSteps):
	laststep = {0: 0, 1: 1, 2: 2, 3: 4}

	if numSteps < 0:
		return 0
	
	if numSteps < 4 and numSteps >= 0:
		return laststep[numSteps]

	prevStep = laststep[3]
	prev2Step = laststep[2]
	prev3Step = laststep[1]

	for i in range(4, numSteps + 1):
		currentCount = prevStep + prev2Step + prev3Step

		prevStep, prev2Step, prev3Step = currentCount, prevStep, prev2Step


	return currentCount

import unittest
class TestClass(unittest.TestCase):
	def test_tripleStep(self):
		self.assertEqual(TripleStep(3), 4)
		self.assertEqual(TripleStep(7), 44)

if __name__ == "__main__":
	unittest.main()
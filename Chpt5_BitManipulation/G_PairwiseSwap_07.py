EVEN = 0x5555555555555555
ODD  = 0xAAAAAAAAAAAAAAAA

def pairwiseSwap(n):
  return ((n & ODD) >> 1) + ((n & EVEN) << 1)

import unittest

class Test(unittest.TestCase):
  def test_pairwiseSwap(self):
    self.assertEqual(pairwiseSwap(0), 0)
    self.assertEqual(pairwiseSwap(42), 21)
    self.assertEqual(pairwiseSwap(21), 42)
    self.assertEqual(pairwiseSwap(43), 23)
    self.assertEqual(pairwiseSwap(EVEN), ODD)
    self.assertEqual(pairwiseSwap(511), 767)
    self.assertEqual(pairwiseSwap(1023), 1023)

if __name__ == "__main__":
  unittest.main()
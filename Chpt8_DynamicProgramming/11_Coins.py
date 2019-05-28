def coins1(total):
	coins = [1,5,10,25]

	dp = [[0 for x in range(len(coins))] for i in range(total + 1)]
	
	for index, coin in enumerate(coins):
		dp[0][index] = 1

	for cost in range(1, total+1):
		for coinIndex, coin in enumerate(coins):
			if cost >= coin:
				dp[cost][coinIndex] += dp[cost - coin][coinIndex]

			if coinIndex > 0:
				dp[cost][coinIndex] += dp[cost][coinIndex - 1]

	return dp[total][3]

def coins2(total):
	coins = [1,5,10,25]
	dp = [1] + [0 for x in range(total)]


	for index, coin in enumerate(coins):
		for amount in range(coin, total+1):
			dp[amount] += dp[amount - coin]

	return dp[total]


import unittest
class Test(unittest.TestCase):
  def test_coins1(self):
    self.assertEqual(coins1(0), 1)
    self.assertEqual(coins1(1), 1)
    self.assertEqual(coins1(4), 1)
    self.assertEqual(coins1(5), 2)
    self.assertEqual(coins1(15), 6)
    self.assertEqual(coins1(17), 6)
    self.assertEqual(coins1(20), 9)
    self.assertEqual(coins1(25), 13)
    self.assertEqual(coins1(52), 49)
    self.assertEqual(coins2(0), 1)
    self.assertEqual(coins2(1), 1)
    self.assertEqual(coins2(4), 1)
    self.assertEqual(coins2(5), 2)
    self.assertEqual(coins2(15), 6)
    self.assertEqual(coins2(17), 6)
    self.assertEqual(coins2(20), 9)
    self.assertEqual(coins2(25), 13)
    self.assertEqual(coins2(52), 49)
  
 

if __name__ == "__main__":
  unittest.main()

def BalloonBurst(array):

	nums = [1] + array + [1]

	dp = [[0] * len(num) for x in range(len(num))]

	left, right = 0

	for balloonRange in range(1, len(nums) - 1): #iterate through balloons, excluding +1 added on each side, this is the size of the gap/range to look at
		for left in range(0, len(nums) - balloonRange - 1): #calculate number of iterations of gap size you can do
			right = left + 1 + balloonRange #starts at first index after size of balloon range
				for k in range(left + 1, right):  #left and right values are excluded from range calc
					dp[left][right] = max(dp[left][right], 
						nums[k] * nums[left] * nums[right] + dp[left][k] + dp[k][right])

	return dp[0][-1]


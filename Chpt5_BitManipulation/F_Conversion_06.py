def conversion(num1, num2):
	numIntersect = num1 ^ num2

	count = 0

	while numIntersect != 0:
		if numIntersect & 1 == 1:
			count += 1
			
		numIntersect >>= 1

	return count
import pdb

def oneAway(str1, str2):
	stepCount = 0
	shortcharindex = 0

	if len(str1) >= len(str2):
		longstr, shortstr = str1, str2
	else:
		longstr, shortstr = str2, str1

	longstrLength = len(longstr)
	shortstrLength = len(shortstr)

	if longstrLength - shortstrLength > 1:
		return False

	for longcharindex in range(longstrLength):
		if shortcharindex > shortstrLength - 1 or shortstr[shortcharindex] != longstr[longcharindex]:
			stepCount += 1
			if stepCount > 1:
				return False
			if longstrLength > shortstrLength:
				longcharindex += 1	
		shortcharindex += 1
	
	return stepCount <= 1


if __name__ == "__main__":
	import sys
	print(oneAway(sys.argv[-2], sys.argv[-1]))		

def check_permutation(string1, string2):
	if len(string1) != len(string2):
		return False

	counter = Count()

	for letter in string1:
		counter[letter] += 1

	for letter in string2:
		if counter[letter] == 0:
			return False
		counter[letter] -= 1

	return True



class Count(dict):
	def __missing__(self, key):
		return 0

# __missing__ defines function return if key is not present in dictionary

if __name__ == "__main__":
	import sys
	print(check_permutation(sys.argv[-1], sys.argv[-2]))
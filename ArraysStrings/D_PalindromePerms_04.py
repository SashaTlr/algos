def pal_perms(string):
	
	charBools = CharBools()
	counter = 0
	
	for char in string:
			charBools[char.lower()] = not charBools[char.lower()]

	for item in charBools.values():
		if not item:
			counter += 1
		if counter > 1:
			return False

	return len(string) % 2 == counter

#does not take into account special chars



class CharBools(dict):
	def __missing__(self, key):
		return True


if __name__ == "__main__":
	import sys
	print(pal_perms(sys.argv[-1]))
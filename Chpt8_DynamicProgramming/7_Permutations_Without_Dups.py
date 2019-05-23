def string_perms(word):
	if word is None:
		 return word

	return string_perms_helper(word, "")

def string_perms_helper(word, prefix):
	permutations = []
	if len(word) == 1:
		permutations += [prefix + word]

	for (index, char) in enumerate(word):
		permutations += string_perms_helper(word[:index] + word[index+1:], prefix + char)
	return permutations


import unittest
class TestCase(unittest.TestCase):
	
	def test_string_perms(self):
		self.assertEqual(len(string_perms('abc')), 6)
		self.assertEqual(len(string_perms('abcd')), 24)


if __name__ == "__main__":
	unittest.main()

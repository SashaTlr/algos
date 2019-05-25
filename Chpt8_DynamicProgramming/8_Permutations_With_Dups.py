# #perms with dupes

# #create a hashset of all characters in string

# #create list of all of the keys in the hashset

# #to avoid creating dupes, create all possible strings where prefix is one value plus rest of hashset

# #add back prefix and move to next character

# #delete character after last one is used (ie count is now 0 or 1..?)

def perms_with_dupes(word):

	if len(word) <= 1 or word is None:
		return word

	charSet = get_char_set(word)
	results = []

	perms_with_dupes_recurse('', charSet, len(word), results)

	return results

def perms_with_dupes_recurse(word, charSet, n, results):

	if len(word) == n:
		results.append(word)

	for char in charSet:
		if charSet[char] == 1:
			del charSet[char]
		else:
			charSet[char] -= 1

		perms_with_dupes_recurse(word + char, charSet, n, results)
		
		if char not in charSet:
			charSet[char] = 1
		else:
			charSet[char] += 1

def get_char_set(word):
	charSet = {}
	for char in word:
		if char not in charSet:
			charSet[char] = 1
		else:
			charSet[char] += 1

	return charSet

import unittest
class TestCase(unittest.TestCase):
	testCase = "aabb"
	expectation = "abba", "aabb", "bbaa", "baba", "abab", "baab"

	def test_perms_with_dupes(self):
		self.assertEqual(set(perms_with_dupes(self.testCase)), set(self.expectation))

if __name__ == "__main__":
	unittest.main()




def paren(n):
	if n == 0:
		return ''
	else:
		return paren_recurse(n, n)

	return parens_list


def paren_recurse(leftRem, rightRem, word = None):
	parens = []
	if leftRem <= 0 and rightRem <= 0:
		parens += [word]

	if leftRem > 0:
		if word is None:
			word = ''
		parens += paren_recurse(leftRem - 1, rightRem, word +'(')

	if rightRem > 0 and rightRem > leftRem:
		parens += paren_recurse(leftRem, rightRem - 1, word + ')')

	return parens

import unittest
class TestCase(unittest.TestCase):
	expectation1 = ["()"]
	expectation2 = ["()()", "(())"]
	expectation3 = ["()()()", "()(())", "(())()", "(()())", "((()))"]

	def test_paren(self):
		self.assertEqual(set(parens(1)), set(self.expectation1))
    	self.assertEqual(set(parens(2)), set(self.expectation2))
    	self.assertEqual(set(parens(3)), set(self.expectation3))



if __name__ == "__main__":
	unittest.main()

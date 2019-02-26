import unittest

def IsRotation(str, substr):
	if len(str) != len(substr):
		return False

	return IsSubstring(str + str, substr)


def IsSubstring(str, substr):
	return substr in str


class Test(unittest.TestCase):
	testdata = [
		("waterbottle", "bottlewater", True),
		("water", "waterbottle", False),
		("waterbottle", "bottlewaler", False)]

	def test_IsRotation(self):
		for [substring, string, expected] in self.testdata:
			actual = IsRotation(string, substring)
			self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()

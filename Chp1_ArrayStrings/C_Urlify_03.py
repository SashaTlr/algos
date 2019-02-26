def escape_characters(str, truelength):
	string = list(str)
	#count number of spaces
#	if truelength == 0:
#		return string

	numSpaces = 0

	for i in range(0, truelength, 1):
		if string[i] == " ":
			numSpaces += 1

	urlStringLen = truelength + numSpaces * 2


	if urlStringLen > len(string):
		raise ValueError("string is invalid length")

	stringDiff = numSpaces * 2 

	for i in range(urlStringLen-1, 0, -1):
		if string[i - stringDiff] != " ":
			string[i] = string[i - stringDiff]
		else:
			string[i] = "%"
			string[i-1] = "0"
			string[i-2] = "2"
			stringDiff -= 2

	return "".join(string).strip()

if __name__ == "__main__":
	import sys
	print(escape_characters(sys.argv[-2], sys.argv[-1]))


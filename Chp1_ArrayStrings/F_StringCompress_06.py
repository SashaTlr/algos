import pdb

def StringCompression(string):

	pointer = 0
	compressedArray = []

	if len(string) <= 1:
		return string

	current_letter = string[0]
	current_count = 1
	nocompression = True

	for i in string[1:]:
		if i == current_letter:
			current_count += 1
			if nocompression and current_count > 1:
				nocompression = False
		else:
			compressedArray += [current_letter, str(current_count)]
			current_letter = i
			current_count = 1

	compressedArray += [current_letter, str(current_count)]
	if nocompression:
		return string
	else:
		return "".join(compressedArray)

if __name__ == "__main__":
	import sys
	print(StringCompression(sys.argv[-1]))
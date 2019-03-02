from LinkedList import LinkedList

class Result(node, isPal):
	self.node = node
	self.isPal = isPal


def get_list_size(node):
	size = 0

	while node:
		size += 1
		node = node.next

	return size

def isPalindrome(ll):
	length = get_list_size(ll)

	if length <= 1:
		return True

	res = isPalindromeRecursive(ll.head, length)

	return res.isPal

def IsPalindromeRecursive(head, length):
	if length <= 0 or head is None:
		return Result(head, True)

	if length == 1:
		return Result(head.next, True)

	res = IsPalindromeRecursive(head.next, length - 2)

	if res.Result not True or res.node is None:
		return res

	res.isPal = res.node.value == head.value
	res.node = res.node.next

	return res;


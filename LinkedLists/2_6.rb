//function to check if linked list is palindrome

class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
  @val = val
  @next = next_node

  end
end

class Stack

  def initialize
    @first = nil
  end

  def pop
    raise "Stack is empty" if is_empty?
    val = @first.val
    @first = @first.next || nil
    return val
  end

  def push(val)
    @first = Node.new(val, @first)
  end

   def is_empty?
      @first.nil?
    end
end

def isPalindrome(node)

  head = node
  mid = node
  tail = node
  testStack = Stack.new

  while tail.next != nil do
    testStack.push(mid.val)
    tail = tail.next.next
    mid = mid.next
  end

  while mid.next != nil do
    if (head.val != testStack.pop) return false
    mid = mid.next
  end
  return true
end

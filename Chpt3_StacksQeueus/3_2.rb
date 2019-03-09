//add stack min to function with O(1)

class Node
  attr_accessor :value, :next

  def initialize(value, next_node)
    @value = value
    @next = next_node
  end
end

class Stack

  attr_accessor :first
  def initialize(node)
    @first = node
  end

  def pop
    raise "Stack is empty" if is_empty?
    val = @first.val
    @first = @first.next || nil
    return val
  end

  def push(val)
    @first = Node(val, @first)
  end

  def is_empty?
    @first.nil?
  end

end

class StackMin
  attr_accessor :stack, :min_stack
  def initialize
    @stack = Stack.new(Node.new(value, nil))
    @min_stack = Stack.new(Node.new(value, nil))
  end

  def push(value)
    stack.push(value)
    if min_stack.first.value > value then min_stack.push(value)
  end

  def pop
    if stack.first.value == min_stack.first.value
      stack.pop()
      min_stack.pop()
    else
      stack.pop()
    end
  end

  def min
    min_stack.first.value
  end
end


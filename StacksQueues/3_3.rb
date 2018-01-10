// Stack of plates
class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
    @val = val
    @next = next_node
  end
end

class Stack
  attr_accessor :first

  def initialize(val)
    @first = Node.new(val, nil)
  end

  def pop
    raise "Stack is empty" if @first.nil?

    val = @first.val
    @first = @first.next

    return val
  end

  def push(val)
    @first = Node(val, @first)
  end
end

class SetOfStacks
  attr_accessor :limit, :stack_count

  def initialize(limit)
    @limit = limit
    @stack_set = []
    @stack_set_count = 0
    @stack_count = 0
    @stack = nil
  end

  def push(val)
    if @stack.nil? || @stack_count >= @limit
      @stack_count = 1
      @stack_set_count += 1
      @stack = Stack.new(val)
      @stack_set[@stack_set_count] = @stack
    else
      @stack.push(val)
      @stack_count += 1
      @stack_set[@stack_set_count] = @stack
    end
  end

  def pop
    if @stack_set_count == 1 && @stack_count == 1
      @stack.pop
      @stack_set_count = 0
      @stack_set = nil
      @stack_count = 0
    elsif @stack_count == 1
      @stack.pop
      @stack_count = @limit
      @stack_set[@stack_set_count] = nil
      @stack_set_count -= 1
    else
      @stack.pop
      @stack_count -= 1
    end
  end
end

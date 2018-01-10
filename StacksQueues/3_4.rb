//queue is FIFO
class Node
  attr_accessor :value, :next

  def initialize(val, next_node)
    @value = val
    @next = next_node
  end
end

class Queue
  attr_acccessor :first, :last

  def initialize(val, nil)
    @first = Node.new(val, nil)
    @last = @first
  end

  def isEmpty
    @first == @last
  end

  def peek
    if !isEmpty then @first.val
  end

  def remove()
    if !isEmpty
      val = @first.val
      @first.val = @first.next.val
      @first.next = @first.next.next
      return val
  end

  def add(item)
    @last.next = Node.new(item, nil)
    @last = @last.next
  end

end

//queue vs stacks
//implement a queue using two stacks

//queue is first in first out
//stack is first in last out
//add to one stack
//when remove, pop stack out to next stack
//remove last entry
//keep contents in second stack until depleted on pops
//keep adding to new stack (instead of swapping stacks every operation)
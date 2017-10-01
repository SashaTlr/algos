class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
    @val = val
    @next = next_node
  end
end

def addList(node1, node2)
  pointer1 = node1
  pointer2 = node2
  carryover = 0
  tail = nil

  while (pointer1 != nil || pointer2 != nil) do
    val1 = pointer1.val || 0
    val2 = pointer2.val || 0
    carryover = (val1 + val2 + carryover) > 9 ? 1 : 0
    tail = Node.new((val1 + val2 + carryover) % 10, tail)
    end
  end
end


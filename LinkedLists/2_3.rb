//delete middle node
class Node
  attr_accessor :next, :val

  def initialize(val, next_node)
    @val = val
    @next = next_node
  end
end

def delete_node(node)
  if node.next = nil then return nil

  node.val = node.next.val
  node.next = node.next.next

end

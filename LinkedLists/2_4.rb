class Node
  attr_accessor :next, :val

  def initialize( val, next_node)
    @val = val
    @next = next_node
  end
end

def partition_list(node, threshold)
head = node
tail = node

  while (node != nil) do
    nextNode = node.next
    if node.val < threshold
      node.next = head
      head = node
    else
      tail.next = node
      tail = node
    end

    node = nextNode
  end

  tail.next = nil
  return head
end

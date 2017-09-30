//implement an algorithm to find kth to last element of a singly
//linked list
class Node
    attr_accessor :val, :next

  def initialize (val, next_node)
    @val = val
    @next = next_node
  end

end


def delete_kth(head, k)
  pointer = head

  k.times do |i|
    pointer = pointer.next
  end

  kpointer = head
  while pointer.next != nil do
    pointer = pointer.next
    kpointer = kpointer.next
  end

kpointer.next = kpointer.next.next

return head

end
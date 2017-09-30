//remove dupes from unsorted linked list

class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
    @val = val
    @next = next_node
  end
end

//delete dupes

def delete_dups(head)
  dataHash = Hash.new
  dataHash[head.val] = true;

  pointer = head;

  while (pointer.next != nil) do
    if dataHash.key?(pointer.next.val)
      pointer.next = pointer.next.next
    else
      dataHash[pointer.next.val] = true
    end
    pointer = pointer.next
  end

end

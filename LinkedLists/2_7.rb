class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
  @val = val
  @next = next_node

  end
end

//find intersection of list

def intersection(node1, node2)
  head1 = node1
  head2 = node2

  while (head1.next != nil && head2.next != nil)
    {
      head1 = node1.next
      head2 = node2.next
    }

  startpointer = head1.next == nil ? node1 : node2
  midpointer = head1.next == nil ? head2 : head1
  longnode = head1.next == nil ? node2 : node1

  while midpointer != nil
    {
        longnode = longnode.next
        midpointer = midpointer.next
    }

intersection = false
  while longnode != nil
    {
      if longnode == startpointer
        return true
      end
    }

    return intersection
end

//Loop detection

//go double time...

class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
  @val = val
  @next = next_node

  end
end

def collision(node)

//move two pointers, one 2x

//when nodes are equal, set pointer to collision, set pointer to beginning,
//fast node is behind slow node by loop size - k when slow pointer enters loop, will catch up in loop size - k steps
// iterate through two pointers, they meet at loop start

end
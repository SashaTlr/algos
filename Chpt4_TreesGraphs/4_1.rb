//undirected graph

class Node

  attr_accessor :val, :adjacents

  def initialize(val)
    @val = val
    @adjactents = Set.new
  end

  def to_s
    @val
  end

end

class Graph

  def add_edge(node_a, node_b)
    node_a.adjacents << node_b
    node_b.adjacents << node_a
  end
end


# breadth-first search

class BreadFirstSearch

  def initialize(graph, source_node)
    @graph = graph
    @node = source_node
    @visited = []
    @edge_to = {}

    bs(source_node)
  end

  def shortest_path_to(node)
    return unless has_path_to?(node)

    path = []

    while (node != @node) do
      path.unshift(node) #adds first node in array
      node = @edge_to[node]
    end

    path.unshift(@node)
  end


  private

  def bs(node)
    queue = [] #queue is an array in Ruby
    queue << node # put source node in queue
    @visited << node # put source node in visited

    while queue.any?
      current_node = queue.shift
      current_node.adjacents.each do |adjacent_node|
        next if @visited.include?(adjacent_node) #go to next adjacent node if it's already been visited
          queue << adjacent_node #not visited, add to queue end
          @visited << adjacent_node #mark as visited
          @edge_to[adjacent_node] = current_node
      end
    end
  end

  def has_path_to?(node)
    @visited.include?(node)
  end

end
//animal shelter
//FIFO

class Animal < Struct.new(value, next)
  attr_accessor :time
  def initialize
    @time = Date.Now
  end
end

class Dog < Animal
end

class Cat < Animal
end

class AnimalQueue
attr_accessor :dogs :cats

  def initialize
    @dogs = LinkedList(nil)
    @cats = LinkedList(nil)
  end

  def enqueue(animal)
    if animal.is_a? Dog
      @dogs.add(animal)
    else
      @cats.add(animal)
    end
  end

  def dequeueAny
    if @dogs.isEmpty? && !@cats.isEmpty?
      return @cats.pop
    if @cats.isEmpty? && !@dogs.isEmpty?
      return @dogs.pop
    if @dogs.peek.time < @cats.peek.time
      @dogs.pop
    else
      @cats.pop
    end
  end
end
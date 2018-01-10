//sort stack

//pop off one stock and add to other
//can store a temp variable

def sortStack(stack1)
  stack2 = Stack.new

  stack2.push(stack1.pop)

  until stack1.isEmpty? do
    temp = stack1.pop

    count = 0
    until stack2.peek <= temp || stack2.isEmpty?
      stack1.push(stack2.pop)
      count += 1
    end

    stack2.push(temp)
  end

  while (!stack2.isEmpty?) do
    stack1.push(stack2.pop)
  end

end

from stack import Stack

def sortStack(stack1):
    stack2 = Stack()

    size = stack1.size()

    # while stack1.size() > 0:
    while not stack1.size() == 0:
        if stack2.size() == 0:
            stack2.push(stack1.pop())
        else:
            temp = stack1.pop()
            while temp < stack2.peek():
                stack1.push(stack2.pop())
            stack2.push(temp)

    return stack2

def printStack(stack):
    stack2 = Stack()
    size = stack.size()
    for i in range(size):
        stack2.push(stack.pop())
        print stack2.peek()

    for i in range(stack2.size()):
        stack.push(stack2.pop())


def main():
  stack = Stack()
  stack.push(1)
  stack.push(5)
  stack.push(10)
  stack.push(7)
  stack.push(3)

  ret_stack = sortStack(stack)
  printStack(ret_stack)


if __name__ == '__main__':
    main()

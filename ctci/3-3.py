from stack import Stack

class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.set = []
        self.set.append(None)
        self.currentStack = 0

    def push(self, item):
        if self.set[self.currentStack] == None:
            self.set[self.currentStack] = Stack()
            self.set[self.currentStack].push(item)
        else:
            temp = self.set[self.currentStack]
            size = temp.size()
            if  size < self.threshold:
                self.set[self.currentStack].push(item)
            else:
                self.set.append(Stack())
                self.currentStack +=1
                self.set[self.currentStack].push(item)

    def pop(self):
        if self.set[self.currentStack] == None:
            return None
        else:
            ret = self.set[self.currentStack].pop()
            if  self.set[self.currentStack].size() == 0:
                self.set.pop()
                self.currentStack -=1

    def display(self):
        for i in range(self.currentStack+1):
            temp = self.set[i]
            print temp.peek()


def main():
  stacky = SetOfStacks(2)
  stacky.push("1")
  stacky.push("2")
  stacky.push("3")
  stacky.push("4")
  stacky.push("5")
  stacky.push("6")
  stacky.display()
  stacky.pop()
  stacky.pop()
  print "- - - - - -"
  stacky.display()


if __name__ == '__main__':
    main()

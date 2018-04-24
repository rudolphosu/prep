#Optimize: dont copy s2 back to s1 unless enqueue called
from stack import Stack

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def enqueue(self, item):
        self.s1.push(item)
        self.size +=1

    def dequeue(self):
        self.size -=1
        for i in range(self.size):
            self.s2.push(self.s1.pop())
        ret = self.s1.pop()
        for i in range(self.size):
            self.s1.push(self.s2.pop())
        return ret

def main():
  myQ = MyQueue()
  myQ.enqueue(1)
  myQ.enqueue(2)
  print myQ.dequeue()
  print myQ.dequeue()


if __name__ == '__main__':
    main()

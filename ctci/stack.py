class Stack:
     def __init__(self):
         self.items = []

     def __repr__(self):
         return str(self.items)

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         if self.size() < 1:
             return None
         else:
             return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

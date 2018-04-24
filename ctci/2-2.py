def solution(head, k):
    j = 0
    inode = head
    jnode = head
    prevnode = None
    while jnode is not None:
        if j < k:
            jnode = jnode.next
            j+=1
        else:
            prevnode = inode
            inode = inode.next
            jnode = jnode.next
    prevnode.next = inode.next

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def addToTail(self, node):
        tail = node
        node = self
        while node.next is not None:
            node = node.next
        node.next = tail

    def display(self):
        node = self
        while node is not None:
            print node.data
            node = node.next

def main():
    n1 = Node("wha")
    n2 = Node("tih")
    n3 = Node("sup")
    n4 = Node("bih")
    n5 = Node("shiz")
    n6 = Node("!!!")
    n1.addToTail(n2)
    n2.addToTail(n3)
    n3.addToTail(n4)
    n4.addToTail(n5)
    n5.addToTail(n6)

    print solution(n1, 3)

    n1.display()

if __name__ == '__main__':
    main()

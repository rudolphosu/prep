def solution(head, partition):
    node = head
    lhead = None
    rhead = None

    while node is not None:
        if node.data < partition:
            if lhead is None:
                lhead = Node(node.data)
            else:
                temp = Node(node.data)
                lhead.addToTail(temp)
        else:
            if rhead is None:
                rhead = Node(node.data)
            else:
                temp = Node(node.data)
                rhead.addToTail(temp)
        node = node.next


    lhead.addToTail(rhead)
    head = lhead
    return head
    # head.display()

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
    n1 = Node(1)
    n2 = Node(10)
    n3 = Node(3)
    n4 = Node(7)
    n5 = Node(5)
    n6 = Node(6)
    n1.addToTail(n2)
    n2.addToTail(n3)
    n3.addToTail(n4)
    n4.addToTail(n5)
    n5.addToTail(n6)

    n1.display()
    print "- - - - -"

    n1 = solution(n1,7)

    n1.display()

if __name__ == '__main__':
    main()

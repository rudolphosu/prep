def solution(head1, head2):
    if head1.next is None and head2.next is None:
        sum = head1.data + head2.data
        return Node(sum)

    sum = head1.data + head2.data
    deeper = solution(head1.next, head2.next)
    if deeper.data > 9:
        deeper.data = deeper.data % 10
        sum += 1
    node = Node(sum)
    node.next = deeper
    return node

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
    n2 = Node(1)
    n3 = Node(9)
    n4 = Node(7)
    n5 = Node(5)
    n6 = Node(6)
    n1.addToTail(n2)
    n1.addToTail(n3)
    n4.addToTail(n5)
    n4.addToTail(n6)

    sol = solution(n1,n4)

    sol.display()

if __name__ == '__main__':
    main()

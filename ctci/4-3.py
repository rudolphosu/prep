from tree import Node,Tree
import math

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setNext(self,node):
        self.next = node

    def hasNext(self):
        if self.next:
            return True
        else:
            return False

def createTree(list, start = 0, end = None):
    if end == None:
        end = len(list)

    if start == end:
        return

    mid = (start + end)/2
    node = Node(list[mid])
    node.setLeftChild(createTree(list,start,mid))
    node.setRightChild(createTree(list,mid+1,end))

    return node

def createList(treeNode, list, height = 0):
    if not treeNode:
        return

    if list[height]:
        node = list[height]
        while node.getNext():
            node = node.getNext()
        tail = ListNode(treeNode.getData())
        node.setNext(tail)
    else:
        list[height] = ListNode(treeNode.getData())

    createList(treeNode.getLeftChild(), list, height+1)
    createList(treeNode.getRightChild(), list, height+1)

def printList(node):
    while node.getNext():
        print node.getData()
        node = node.getNext()

    print node.getData()

def main():
    list = [1,2,3,4,5,6,7,8,9]

    node = createTree(list)

    listOfLinked = [None for i in range(int(math.ceil(math.log(11,2))))]

    createList(node,listOfLinked)

    for i in range(len(listOfLinked)):
        print "level %s" % (i+1)
        printList(listOfLinked[i])


main()

from tree import Node,Tree
import math

def createTree(list, start = 0, end = None):
    if end == None:
        end = len(list)

    if start == end:
        return

    mid = (start + end)/2
    node = Node(list[mid])
    left = createTree(list,start,mid)
    right = createTree(list,mid+1,end)
    if left:
        left.setParent(node)
    if right:
        right.setParent(node)
    node.setLeftChild(left)
    node.setRightChild(right)

    return node

def commonAncestor(node1,node2):
    print node1.getData(), node2.getData()
    start1 = node1
    start2 = node2

    # find height1
    height1 = 0
    while(node1.getParent()):
        height1+=1
        node1 = node1.getParent()

    # find height2
    height2 = 0
    while(node2.getParent()):
        height2+=1
        node2 = node2.getParent()

    # move lower node up by difference in height1
    difference = height1 - height2
    if difference > 0:
        for i in range(difference):
            start1 = start1.getParent()
    elif difference < 0:
        for i in range(abs(difference)):
            start2 = start2.getParent()

    # advance together until at same node
    while start1:
        print start1.getData(), start2.getData()
        if start1.getData() == start2.getData():
            return start1.getData()
        start1 = start1.getParent()
        start2 = start2.getParent()

    return None

def main():
    list = [1,2,3,4,5,6,7,8,9]

    node = createTree(list)

    print node

    right1 = node.getRightChild()
    right2 = right1.getRightChild()
    right1left1 = right1.getLeftChild()
    left1 = node.getLeftChild()

    print commonAncestor(left1,right2)
    print commonAncestor(right1left1,right2)



main()

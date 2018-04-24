from tree import Node,Tree

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
        left.setParent = node
    if right:
        right.setParent = node
    node.setLeftChild(left)
    node.setRightChild(right)

    return node

def successorHelper(node):

    if node.getLeftChild():
        return successorHelper(node.getLeftChild())
    else:
        if node.getParent():
            parent = node.getParent()
            if node.getRightChild():
                parent.setLeftChild(node.getRightChild())
            else:
                parent.setLeftChild(None)

        return node

def inOrderSuccessor(node):
    if node.getRightChild():
        suc = successorHelper(node.getRightChild())
        return suc
    else:
        child = node
        parent = child.getParent()
        while parent and not parent.getLeftChild() == child:
            child = parent
            parent = parent.getParent()
        return child

def main():
    list = [1,2,3,4,5,6,7,8,9]

    node = createTree(list)

    print node

    print successor(node).getData()


    print "- - - - -"


    rightChild1 = node.getRightChild()
    rightChild1.setLeftChild(None)

    print node

    print successor(node).getData()



main()

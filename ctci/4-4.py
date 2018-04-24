from tree import Node,Tree

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

def balanced(node):
    if not node:
        return 0

    left = balanced(node.getLeftChild())
    right = balanced(node.getRightChild())
    if left - right not in [-1,0,1]:
        return float('-inf')

    sum = 1 + max(left,right)
    return sum

def balanceFactor(node):
    if not node:
        return True

    left = balanced(node.getLeftChild())
    right = balanced(node.getRightChild())
    bF = left - right


    if bF < -1 or bF > 1:
        return False

    return True

def main():
    list = [1,2,3,4,5,6,7,8,9]

    node = createTree(list)
    print node
    print balanceFactor(node)

    node2 = Node(0)
    node3 = Node(1)
    node2.setRightChild(node3)
    node3.setRightChild(Node(2))
    node3.setLeftChild(Node(3))
    print node2
    print balanceFactor(node2)

    node4 = Node(4)
    node2.setLeftChild(node4)

    print node2
    print balanceFactor(node2)

    node5 = Node(5)
    node6 = Node(6)

    node4.setRightChild(node5)
    node5.setRightChild(node6)

    print node2
    print balanceFactor(node2)

    node

main()

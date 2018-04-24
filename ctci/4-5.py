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

def validateBST(node,min,max):
    if not node:
        return True

    val = node.getData()
    if val < min or val > max:
        return False

    left = validateBST(node.getLeftChild(), min, node.getData())
    right = validateBST(node.getRightChild(), node.getData(), max)

    return left and right

def main():
    list = [1,2,3,4,5,6,7,8,9]

    node = createTree(list)
    print node
    print validateBST(node,float('-inf'),float('inf'))

    rightChild1 = node.getRightChild()
    leftChild1 = rightChild1.getLeftChild()
    leftChild2 = leftChild1.getLeftChild()
    leftChild2.setData(4)

    print node
    print validateBST(node,float('-inf'),float('inf'))

main()

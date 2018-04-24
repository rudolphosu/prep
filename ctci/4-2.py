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

def main():
    list = [1,2,3,4,5,6,7,8,9]

    node = createTree(list)
    print node

main()

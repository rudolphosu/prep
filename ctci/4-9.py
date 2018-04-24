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

def treeToLists(node,lists,height = 0):
    if not node:
        return
    lists[height].append(node.getData())
    treeToLists(node.getLeftChild(),lists,height+1)
    treeToLists(node.getRightChild(),lists,height+1)

def permutations(inList,retlist,start=0):
    if start == len(inList):
        temp = [ch for ch in inList]
        retlist.append(temp)
        return

    for i in range(start,len(inList)):
        inList[start],inList[i] = inList[i],inList[start]
        permutations(inList,retlist,start+1)
        inList[i],inList[start] = inList[start],inList[i]

def computeCombine(lists,retList):
    index = 1
    while index < len(lists):
        perms = []
        permutations(lists[index],perms)
        temp = []
        for l1 in retList:
            for l2 in perms:
                temp.append(l1+l2)
        retList = temp
        index+=1
    return retList

def main():
    list = [1,2,3,4,5,6,7]
    node = createTree(list)

    height = int(math.floor(math.log(6,2))+1)
    lists = [[] for i in xrange(height)]

    treeToLists(node,lists)

    retList = [[lists[0][0]]]
    print computeCombine(lists,retList)

main()

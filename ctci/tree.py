class Tree:
    def __init__(self, root = None):
        self.root = root

    def __repr__(self):
        return repr(self.root)

class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setLeftChild(self,child):
        self.leftChild = child

    def setRightChild(self,child):
        self.rightChild = child

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setParent(self,parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __repr__(self):
        ret = '('
        if self.leftChild:
            ret = ret + repr(self.leftChild)
        ret = ret + str(self.data)
        if self.rightChild:
            ret = ret + repr(self.rightChild)
        ret = ret + ')'
        return ret

def main():
    root = Node("3")
    tree = Tree(root)
    left1 = Node("2")
    right1 = Node("5")
    root.setLeftChild(left1)
    root.setRightChild(right1)
    left2 = Node("1")
    right2 = Node("4")
    left1.setLeftChild(left2)
    right1.setLeftChild(right2)

    print tree

#did it "backwards" -> end is first point finalized
class point:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __repr__(self):
        return "point is %s, %s" % (self.i,self.j)

    def __eq__(self, other):
        if isinstance(other, point):
          return ((self.i == other.i) and (self.j == other.j))
        else:
          return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

def solution(matrix, iposition, jposition, path, failedSet):
    pt = point(iposition,jposition)
    print(pt)

    # see if we've been here
    if pt in failedSet:
        print "been here " + str(pt)
        return False

    if iposition < 0 or jposition  < 0 or matrix[iposition][jposition] == 1:
        return False

    #if end, return true
    if iposition == 0 and jposition == 0:
        path.append([iposition,jposition])
        return True

    failedSet.add(pt)

    #try move left, append to path if true
    if solution(matrix,iposition,jposition-1,path, failedSet):
        path.append([iposition,jposition])
        return True

    #try move up, append to path if true
    if solution(matrix,iposition-1,jposition,path, failedSet):
        path.append([iposition,jposition])
        return True

    return False

def printMatrix(matrix):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[0])):
            row = row + str(matrix[i][j]) + " "
        print row
    print " "

def createMatrix(m,n):
    matrix = [[0 for x in range(n)] for y in range(m)]
    # for j in range(len(matrix)):
    #     matrix[j][1] = 1
    # for i in range(len(matrix[0])):
    #     matrix[0][i] = 1
    # matrix[1][2] = 1
    matrix[1][0] = 1
    matrix[1][1] = 1
    # matrix[2][3] = 1
    return matrix

def main():
    m,n = 5,5
    Matrix = createMatrix(m,n)
    printMatrix(Matrix)
    path = []
    failedSet = set()
    solution(Matrix,m-1,n-1,path,failedSet)
    print path
    # printMatrix(ret)


if __name__ == '__main__':
    main()

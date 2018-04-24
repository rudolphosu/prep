#quadrants only works for even n
#do layered approach, outer to inner
class Solution(object):
    def rotate90(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        # for i in range(m):
        for i in range(m/2):
            for j in range(n/2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[m-j-1][i]
                matrix[m-j-1][i] = matrix[m-i-1][n-j-1]
                matrix[m-i-1][n-j-1] = matrix[j][m-i- 1]
                matrix[j][m-i-1] = temp
        return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[0])):
            row = row + str(matrix[i][j]) + " "
        print row
    print " "

def createMatrix(m,n):
    matrix = [[0 for x in range(n)] for y in range(m)]
    for j in range(len(matrix)):
        matrix[j][1] = 1
    for i in range(len(matrix[0])):
        matrix[0][i] = 1
    return matrix

def main():
    Matrix = createMatrix(6,6)
    printMatrix(Matrix)
    ret = Solution().rotate90(Matrix)
    printMatrix(ret)


if __name__ == '__main__':
    main()

import time

def matrixSearch(matrix,x):
    m = len(matrix)-1
    n = len(matrix[0])-1
    calculations = 0
    return matrixSearchRecurse(matrix,0,m,0,n,x,calculations)

def matrixSearchRecurse(matrix,row_low,row_up,col_low,col_up,x,calculations):
    if matrix[row_low][col_low] == x:
        # print calculations
        return calculations

    if row_low == row_up == col_low == col_up:
        return calculations

    for i in range(row_low,row_up+1):
        calculations +=1
        low = matrix[i][col_low]
        up = matrix[i][col_up]
        if low > x:
            row_up = i-1
        if up < x:
            row_low = i+1
        if low == x:
            # print calculations
            return  calculations
        if up == x:
            # print calculations
            return calculations

    for j in range(col_low,col_up+1):
        calculations +=1
        low = matrix[row_low][j]
        up = matrix[row_up][j]
        if low > x:
            col_up = j-1
        if up < x:
            col_low = j+1
        if low == x:
            # print calculations
            return  calculations
        if up == x:
            # print calculations
            return calculations

    # printMatrix(matrix,row_low,row_up,col_low,col_up)
    return matrixSearchRecurse(matrix,row_low,row_up,col_low,col_up,x,calculations)

def printMatrix(matrix):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[0])):
            row = row + str(matrix[i][j]) + " "
            if matrix[i][j] < 10:
                row = row+" "
        print row
    print " "

def traverseMatrix(matrix):
    calc1,calc2,calc3 = 0,0,0
    start1_time = time.time()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            calc1 += matrixSearch(matrix,matrix[i][j])
    end1_time = time.time()

    start2_time = time.time()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            calc2 += bruteMatrix(matrix,matrix[i][j])
    end2_time = time.time()

    start3_time = time.time()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            calc3 += bookSearch(matrix,matrix[i][j])
    end3_time = time.time()

    print "time with my search: " + str(end1_time - start1_time)
    print "visits with my search: " + str(calc1)
    print "time with brute search: " + str(end2_time - start2_time)
    print "visits with brute search: " + str(calc2)
    print "time with books search: " + str(end3_time - start3_time)
    print "visits with books search: " + str(calc3)

def bruteMatrix(matrix,x):
    calc = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            calc += 1
            if matrix[i][j] == x:
                return calc

def bookSearch(matrix,x):
    i = 0
    j = len(matrix[0])-1
    calculations = 0
    while j > 0 or i < len(matrix):
        calculations +=1
        if matrix[i][j] == x:
            return calculations
        elif matrix[i][j] < x:
            i+=1
        elif matrix[i][j] > x:
            j-=1

def printMatrix(matrix,row_low,row_up,col_low,col_up):
    print row_low,row_up,col_low,col_up
    if row_up < 6:
        row_up +=1
    if col_up < 6:
        col_up +=1
    for i in range(row_low,row_up):
        row = ""
        for j in range(col_low,col_up):
            row = row + str(matrix[i][j]) + " "
            if matrix[i][j] < 10:
                row = row+" "
        print row
    print " "

def createMatrix(m,n):
    matrix = [[0 for x in range(n)] for y in range(m)]
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            matrix[i][j] = (i+2)*(j+1)
    return matrix

def main():
    Matrix = createMatrix(10,10)
    # printMatrix(Matrix,0,60,0,60)
    # print matrixSearch(Matrix,20)
    traverseMatrix(Matrix)

if __name__ == '__main__':
    main()

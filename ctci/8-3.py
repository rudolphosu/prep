def slowSolution(mArray, index):
    if(mArray[index] == index):
        return index
    else:
        return slowSolution(mArray, index+1)

def fastSolution(marray,start,end):
    if start == end:
        return -1
    mid = (start+end)/2
    if marray[mid] == mid:
        return mid
    elif marray[mid] > mid:
        return fastSolution(marray, mid+1, end)
    else:
        return fastSolution(marray,start,mid-1)

def main():
    magicArray = [-11,-1,2,10,11]
    print magicArray
    print slowSolution(magicArray,0)
    print "----"
    print fastSolution(magicArray,0,len(magicArray))


if __name__ == '__main__':
    main()

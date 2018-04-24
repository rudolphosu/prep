# improvement: dont sequentially search for length after invalid doubling
# instead, send bsearch start = index/2, end = index.. if valAtmid == -1 then high = mid -1 
def searchNoSize(listy,x):
    i = 1
    searching = True
    length = 0
    # find length in logn time
    while searching:
        if not valAt(listy,i) == -1:
            i = i*2
        else:
            i/=2
            while not valAt(listy,i) == -1:
                i+=1
            length = i-1
            searching = False
    return bsearch(listy,0,length,x)

def bsearch(listy,start,end,x):
    print start,end
    mid = (start+end)/2
    if listy[mid] == x:
        return mid
    if start == end:
        return -1
    elif listy[mid] > x:
        return bsearch(listy,start,mid-1,x)
    else:
        return bsearch(listy,mid+1,end,x)

def valAt(listy,index):
    try:
        val = listy[index]
        return val
    except:
        return -1

def main():
    a = []
    for i in range(10):
        a.append(i*2)
    print a

    print searchNoSize(a,18)

if __name__ == '__main__':
    main()

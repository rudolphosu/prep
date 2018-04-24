def bsearchMod(listy,start,end,x):
    while start < end:
        mid = (start+end)/2
        print start,end
        while listy[mid] == '':
            mid +=1
        if listy[mid] > x:
            mid -=1
            while listy[mid] == '':
                mid -=1
            end = mid
        elif  listy[mid] < x:
            # while listy[mid] == '':
            #     print mid
            #     mid +=1
            start = mid
        else:
            return mid

    if listy[end] == x:
        return listy[end]
    else:
        return None

def main():
    a = ["at","","","","ball","","","cat","","","dad","","zzz"]
    print a

    print bsearchMod(a,0,len(a)-1,"at")

if __name__ == '__main__':
    main()

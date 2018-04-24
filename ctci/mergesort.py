def mergeSort(arr):
    print "splitting" + str(arr)
    if len(arr)>1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
            print "merging"+str(arr)


def main():
    arr = [9,4,7,2,8,11,12,1,6]
    mergeSort(arr)
    print arr
main()

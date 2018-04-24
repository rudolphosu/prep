def quickSort(arr,left,right):
    if left<right:
        pivot = partition(arr,left,right)
        quickSort(arr,left,pivot-1)
        quickSort(arr,pivot+1,right)

def partition(arr,left,right):
    pivot = left
    left +=1
    done = False
    while not done:
        while  left <= right and arr[left]<=arr[pivot]:
            left+=1
        while right >= left and arr[right]>=arr[pivot]:
            right-=1
        if right < left:
            done = True
        else:
            arr[left],arr[right] = arr[right],arr[left]
        print arr
    arr[pivot],arr[right] = arr[right],arr[pivot]

    return right


def main():
    arr = [9,4,7,2,8,11,12,1,6]
    quickSort(arr,0,len(arr)-1)
    print arr

main()

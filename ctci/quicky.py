def quicky(list,start,end):
    if start < end:
        pivot = start
        left = pivot+1
        right = end

        done = False
        while not done:
            while left <= right and list[left]<list[pivot]:
                left+=1
            while right >= left and list[right]>list[pivot]:
                right-=1
            if left<=right:
                list[left],list[right] = list[right],list[left]
            else:
                done = True
        list[pivot],list[right] = list[right],list[pivot]
        quicky(list,start,right)
        quicky(list,right+1,end)


def main():
  list = [4,3,6,8,9,5,7,1,2]
  quicky(list,0,len(list)-1)
  print list
main()

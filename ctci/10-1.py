def solution(array,brray):
    helper = []
    for a in range(len(array)/2):
        helper.append(array[a])

    for i in range(len(array)-len(brray),len(array),1):
        array[i] = brray[i-len(brray)]

    left = 0
    middle = len(array)/2
    right = 0
    k = 0
    while left < middle and right < len(brray):
        if helper[left] < brray[right]:
            array[k] = helper[left]
            left+=1
        else:
            array[k] = brray[right]
            right+=1
        k+=1

    while left < middle:
        array[k] = helper[left]
        left+=1
        k+=1

def reverseMerge(array,brray):
    left = len(array)/2-1
    right = len(brray)-1
    k = len(array)-1
    while left >= 0 and right >= 0:
        if array[left] > brray[right]:
            array[k] = array[left]
            left -=1
        else:
            array[k] = brray[right]
            right -=1
        k-=1

    while right >= 0:
        array[k] = brray[right]
        right -=1
        k-=1

def main():
    a = [None]*12
    b = []
    for i in range(1,7,1):
        a[i-1] = i*7
        b.append(i*11)
    # solution(a,b)
    reverseMerge(a,b)
    print a

if __name__ == '__main__':
    main()

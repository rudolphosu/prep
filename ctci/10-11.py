def solution(list):
    for i in range(len(list)-2):
        if list[i] >= list[i+1]:
            if list[i+1] >= list[i+2]:
                list[i+1],list[i+2] = list[i+2],list[i+1]
        elif list[i] <= list[i+1]:
            if list[i+1] <= list[i+2]:
                list[i+1],list[i+2] = list[i+2],list[i+1]
    return list


def main():
    list = [1,5,9,8,6,2,3,4,7]
    print solution(list)

main()

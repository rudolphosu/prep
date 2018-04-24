def solution(string,index,perms):
    if index == len(string):
        temp = [ch for ch in string]
        perms.append(temp)
    for i in range(index,len(string)):
        string[i],string[index] = string[index],string[i]
        solution(string,index+1,perms)
        string[index],string[i] = string[i],string[index]


def main():
    string = "abc"
    stringlist = [ch for ch in string]
    perms = []
    solution(stringlist,0,perms)
    print perms

if __name__ == '__main__':
    main()

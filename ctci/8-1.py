def solution(n, memo):
    if(n == 0):
        return 1
    elif(n<0):
        return 0
    elif not memo[n-1] == None:
        return memo[n-1]
    for i in range(3):
        memo[n-1] = solution(n-1,memo) + solution(n-2,memo) + solution(n-3,memo)
    return memo[n-1]

def main():
    n = 4
    memo = [None for i in range(n)]
    print solution(n, memo)

if __name__ == '__main__':
    main()

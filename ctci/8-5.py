def solution(a,b):
    print "recursed"
    if b==1:
        return a
    else:
        return a + solution(a,b-1)

def main():
    a,b = 5,4
    if a < b:
        result = solution(a,b/2)
        result += result
        if b % 2 == 1:
            result += a
        print result
    else:
        result = solution(b,a/2)
        result += result
        if a % 2 == 1:
            result += b
        print result


if __name__ == '__main__':
    main()

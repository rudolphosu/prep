from stack import Stack

def solution(height,f,t,w):
    if height >= 1:
        solution(height-1,f,w,t)
        t.push(f.pop())
        solution(height-1,w,t,f)

# def solution2(height,f,w,t):
#     if height >= 1:
#         solution2(height-1,f,t,w)
#         t.push(f.pop())
#         solution2(height-1,w,f,t)

def main():
    a,b,c = Stack(),Stack(),Stack()
    a.push(4)
    a.push(3)
    a.push(2)
    a.push(1)
    solution(4,a,c,b)
    print c.size()
    print c

    # solution2(4,a,b,c)
    # print c.size()
    # print c

if __name__ == '__main__':
    main()

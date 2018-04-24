def solution(string,dict,count,perms):
    if count == 0:
        # print string
        temp = [ch for ch in string]
        perms.append(temp)

    for ch in dict.keys():
        if dict[ch] > 0:
            dict[ch] = dict.get(ch)-1
            print dict
            solution(string+ch, dict, count-1, perms)
            dict[ch] = dict.get(ch)+1

def buildDict(string):
    dict = {}
    for ch in string:
        dict[ch] = dict.get(ch,0)+1
    return dict

def main():
    string = "abc"
    dict = buildDict(string)
    print dict
    perms = []

    solution("",dict,len(string),perms)
    print len(perms)
    print perms

if __name__ == '__main__':
    main()

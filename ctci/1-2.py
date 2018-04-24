# O(n)
class Solution1(object):
    def stringReverse(self, string):
        ret = ""
        length = len(string)
        if length < 2:
            return string
        for i in range(length):
            ret = ret + string[length-1-i]
        return ret

class Solution2(object):
    def stringReverse(self, string):
        if len(string) < 2:
            return string

        s = list(string)
        i,j = 0,len(string)-1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        ret = ''.join(s)
        return ret

def main():
    print Solution1().stringReverse("abczdw")
    print Solution2().stringReverse("abczdw")

if __name__ == '__main__':
    main()

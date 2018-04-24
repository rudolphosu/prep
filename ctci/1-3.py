#FEEDBACK
#clarification: case sensitive? whitespace?

class Solution(object):
    def isPermutation(self, string1,string2):
        if not len(string1) == len(string2):
            return False
        stringMap = {}
        for c in string1:
            stringMap[c] = stringMap.get(c,0) + 1

        for ch in string2:
            if not ch in stringMap or stringMap[ch] == 0:
                return False
            stringMap[ch] -=1
        return True

def main():
    print Solution().isPermutation("abzz","zzab")

if __name__ == '__main__':
    main()

#FEEDBACK
#clarification: ascii vs unicode string
#optimization: check if greater than size of alphabet
#bit vector?

#no extra data structures, O(n^2)
class Solution1(object):
    def stringUnique(self, string):
        for i in range(len(string)):
            for c in string[i+1:]:
                if c==string[i]:
                    return False
        return True

#uses set, O(n)
class Solution2(object):
    def stringUnique(self,string):
        chSet = set()
        for c in string:
            if c in chSet:
                return False
            chSet.add(c)
        return True

def main():
    print Solution1().stringUnique("abczdw")
    print Solution2().stringUnique("abczdwt")

if __name__ == '__main__':
    main()

#FEEDBACK: check that size of compression isnt larger than original string
#use list+append instead of string+concat

class Solution(object):
    def compressString(self, string):
        length = len(string)
        if length < 1:
            return string

        ret = ""
        ch = string[0]

        i = 0
        count = 0
        while i < length:
            if not string[i] == ch:
                ret = ret + ch + str(count)
                ch = string[i]
                count = 1
            else:
                count+=1
            i+=1

        return ret + ch + str(count)

def main():
    print Solution().compressString("aabcccccaaa")

if __name__ == '__main__':
    main()

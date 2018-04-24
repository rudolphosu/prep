class Solution(object):
    def replaceWhitespace(self, string):
        ret = ""

        if len(string) < 1:
            return string

        for i in range(len(string.rstrip())):
            if string[i] == ' ':
                ret = ret + "%20"
            else:
                ret = ret + string[i]
        return ret

def main():
    print Solution().replaceWhitespace("Mr John Smith    ")

if __name__ == '__main__':
    main()

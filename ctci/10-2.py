def groupAnagrams(array):
    print array
    # iterate through array, call isAnagram on remaining portion of array
    i=0
    j=1
    matches = 0
    while i < len(array):
        while j < len(array):
            # if array[j] is anagram, swap with array[i+1]
            if isAnagram(array[i],array[j]):
                array[i+1+matches],array[j] = array[j],array[i+1+matches]
                matches +=1
                j+=matches
                # print array
            j+=1
        i+=1
        j = i + 1 + matches
        matches = 0

def groupAnagramsBucket(array):
    bucket = {}
    for string in array:
        key = anaSort(string)
        if not key in bucket:
            bucket[key] = [string]
        else:
            l = bucket.get(key)
            l.append(string)
            bucket[key] = l

    i = 0
    keys = bucket.keys()
    for key in keys:
        vals = bucket[key]
        for j in range(len(vals)):
            array[i] = vals[j]
            i+=1

def anaSort(string):
    chars = [c for c in string]
    chars.sort()
    return ''.join(chars)

def isAnagram(string1,string2):
    dic1 = {}
    dic2 = {}
    for c in string1:
        dic1[c] = dic1.get(c,0)+1
    for c in string2:
        dic2[c] = dic2.get(c,0)+1

    if dic1 == dic2:
        return True
    return False

def main():
    a = []
    a.append("cat")
    a.append("bat")
    a.append("zzz")
    a.append("tac")
    a.append("www")
    a.append("tab")
    a.append("atc")
    # groupAnagrams(a)

    groupAnagramsBucket(a)
    print a

if __name__ == '__main__':
    main()


def lengthOfLongestSubstring(s):
    list1 = []
    max_len = 0
    for i in s:
        if i in list1:
            max_len = max(max_len, len(list1))
            list1 = list1[list1.index(i)+1:]
        list1 += i
    max_len = max(max_len, len(list1))
    return max_len


    # i = 0
    # list1 = []
    # max_len = 0
    # while i < len(s):
    #     if s[i] not in list1:
    #         list1 += s[i]
    #     else:
    #         max_len = max(max_len, len(list1))
    #         list1 = list1[list1.index(s[i])+1:]
    #         list1 += s[i]
    #     max_len = max(max_len, len(list1))
    #     i += 1
    # return max_len

# print(lengthOfLongestSubstring("abcabcbb"))

# print(lengthOfLongestSubstring("bbbbb"))

print(lengthOfLongestSubstring("anviaj"))

# print(lengthOfLongestSubstring("aab"))
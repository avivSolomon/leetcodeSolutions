
def longestCommonPrefix(strs):
    common = []
    min_len = min(len(i) for i in strs)
    i = 0
    while i < min_len:
        cher = [word[i] for word in strs]
        if ''.join(cher) == (cher[0] * len(strs)):
            common += cher[0]
        else:
            break
        i += 1
    return ''.join(common)

print(longestCommonPrefix(["flower","flow","flight"]))



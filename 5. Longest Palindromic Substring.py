
def longestPalindrome(s):
    max_len = s[0]
    n = len(s)
    if n < 2:
        return s
    else:
        i = 0
        for cher in s:
            p1 = []
            if i + 1 < n and cher == s[i + 1]:
                j = 0
                while j <= i and i + j + 1 < n:
                    if s[i - j] == s[i + 1 + j]:
                        p1 = s[i - j:i + 2 + j]
                        j += 1
                    else:
                        break
                if len(p1) > len(max_len):
                    max_len = p1
            if i + 2 < n and cher == s[i + 2]:
                j = 0
                while j <= i and i + j + 2 < n:
                    if s[i - j] == s[i + 2 + j]:
                        p1 = s[i - j:i + j + 3]
                        j += 1
                    else:
                        break
                if len(p1) > len(max_len):
                    max_len = p1
            i += 1
    return max_len

def isPalindrome(s):
    return s == s[::-1]

import math
def longestPalindrome2(s):
    max_len = s[0]
    n = len(s)
    if n < 2:
        return s
    else:
        pivot = [p / 2 for p in range(1, 2 * n - 2)]
        # mpivot = pivot[((n - 2) * 2 + 1) // 2]
        x = [s[int(p) - min(int(p), n - math.ceil(p) - 1):math.ceil(p) + min(int(p), n - math.ceil(p)) + 1] for p in
             pivot]

        for i in x:
            while len(i) > 3:
                if not isPalindrome(i):
                    i = i[1:-1]
                else:
                    break
            if len(i) > len(max_len) and isPalindrome(i):
                max_len = i
        return max_len










print(longestPalindrome2("baba"))
# print(longestPalindrome2("cbbdas"))
print(longestPalindrome2("bb"))
print(longestPalindrome2("ccc"))
# print(longestPalindrome2("xaabacxcabaaxcabaax"))


class Solution:
    def isPalindrome(s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_len = s[0]
        n = len(s)
        if n < 2:
            return s
        else:
            pivot = [p / 2 for p in range(1, 2 * n - 2)]
            x = [s[int(p) - min(int(p), n - math.ceil(p) - 1):math.ceil(p) + min(int(p), n - math.ceil(p)) + 1] for p in
                 pivot]

            for i in x:
                while len(i) > 3:
                    if not isPalindrome(i):
                        i = i[1:-1]
                    else:
                        break
                if len(i) > len(max_len) and isPalindrome(i):
                    max_len = i
            return max_len


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s

        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l - 1:r], s[l:r]

            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1

        return s[start:start + size]


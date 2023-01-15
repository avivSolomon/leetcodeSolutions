# def convert(s, numRows):
#     if (numRows == 1) or len(s) <= numRows:
#         return s
#     n1 = 0
#     n = len(s)
#     if n % numRows != 0:
#         n1 = numRows - (n % numRows)
#     x = [a for a in range(0, n + n1, 2*numRows-2)]
#     ans = [''.join([s[a] for a in x if a < n])]
#     print(s, numRows, x, ans)
#     i = 1
#     while i < numRows:
#         j = i
#         while j < n:
#             cher = [s[j] for a in x if abs(j-a) == i]
#             print(cher)
#             if len(cher) > 1:
#                 ans = ans + [cher[0]]
#             else:
#                 ans = ans + cher
#             j += 1
#         i += 1
#     return ''.join(ans)


# def convert(s, numRows):
#     if numRows == 1:
#         return s
#     else:
#         n = len(s)
#         x1 = [a for a in range(0, n + 2*numRows-2 - (n % numRows), 2*numRows-2)]
#         ans = []
#         i = 0
#         while i < numRows:
#             x = []
#             for a in range(i, n, 2 if numRows - i - 1 > 0 else 2*(numRows-1)):
#                 for j in x1:
#                     if abs(a - j) == i and a not in x:
#                         x = x + [a]
#             ans += [s[a] for a in x]
#             i += 1
#         return ''.join(ans)


def convert(s, numRows):
    if (numRows == 1) or len(s) <= numRows:
        return s
    row = ['']*numRows
    mod = 2*numRows-2
    i = 0                                 #// index cher
    for a in s:
        x = abs((i % mod) - numRows+1)    #// index row
        row[x] = row[x] + a
        i += 1
    row = row[::-1]
    return ''.join(row)


# def convert(s, numRows):
#     if (numRows == 1) or len(s) <= numRows:
#         return s
#     row = ['']*numRows
#     next_row = -1
#     i = 0       #// index row
#     for c in s:
#         row[i] = row[i] + c
#         if i == (('', numRows - 1, 0)[next_row]):
#             next_row *= -1
#         i += next_row
#     return ''.join(row)


def convert(s, numRows):
    if (numRows == 1) or len(s) <= numRows:
        return s
    row = ['']*numRows
    next_row = -1
    t = ('', numRows - 1, 0)
    i = 0       #// index row
    for c in s:
        row[i] += c
        if i == t[next_row]:
            next_row = -next_row
        i += next_row
    return ''.join(row)



# def convert(s, numRows):
#     row = [""] * numRows
#     next_row = 1
#     i = 0
#     for c in s:
#         row[i] += c
#         if next_row == 1 and i == numRows - 1:
#             next_row = -1
#         elif i == 0:
#             next_row = 1
#         i += next_row
#     return "".join(row)



print(convert("PAYPALISHIRING", 3))
print(bool(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"), 3)
print(convert("PAYPALISHIRING", 4))
print(bool(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"), 4)
print(convert("ABCDe", 4))
print(bool(convert("ABCDe", 4) == "ABCeD"), 4)
print(convert('PAYPALISHIRING', 5))
print(bool(convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"), 5)
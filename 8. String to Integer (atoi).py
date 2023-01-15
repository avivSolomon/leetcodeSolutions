#
# def myAtoi(s):
#     ans = ''
#     sig = (' ', '-', '+')
#     for cher in s:
#         if not (cher.isnumeric() or cher in sig) or (ans[-1] in sig[1:] and cher in sig[1:]):
#             break
#         else:
#             ans += cher
#     ans = int(ans) if ans.isnumeric() else 0
#     if abs(ans) > 2147483647:
#         return 2147483647 if ans > 0 else (-2147483648)
#     return ans
#
#
#
# def myAtoi2(s):
#     first = s.split()[0]
#     len1 = len(first)
#     if len1 == 0:
#         return 0
#     i = 0
#     num = '0'
#     negativ = False
#     for char in first:
#         ordCher = ord(char)
#         if ordCher in (43, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57):
#             if i == 0:
#                 i += 1
#                 if char == '-':
#                     if negativ == False:
#                         negativ = True
#                     else: break
#                 elif ordCher in range(48, 58):
#                     num = char
#             else: num += char
#         else: break
#
#     num1 = int(num)
#     max_int = (2 ** 31) - 1
#     min_int = -(2 ** 31)
#     if negativ:
#         num1 *= -1
#         if num1 < min_int:
#             return min_int
#     elif num1 > max_int:
#         return max_int
#     else:
#         return int(num1)



def myAtoi3(s):
    ans = ''
    sig = ""
    for cher in s:
        if cher in ('-', '+', " "):
            if len(sig + ans) == 0:
                sig = cher if cher != ' ' else sig
            else: break
        elif cher.isnumeric():
            ans += cher
        else: break
    ans = 0 if len(ans) == 0 else int(ans)
    if ans > 2147483647:
        return -2147483648 if "-" in sig else 2147483647
    return -ans if "-" in sig else ans

# print(myAtoi3("words and 987"))
print(myAtoi3("-91283472332"))
print(myAtoi3("      -42"))
# print(myAtoi("-+12"))


# def reverse(x):
#     y = abs(x)
#     z = 0
#     while y:
#         z += z * 9 + y % 10
#         y = y // 10
#
#     maxInt = 2 ** 32
#     if z > maxInt:
#         z = 0
#     elif x < 0:
#         z = -z
#     return z




# def reverse(x):
#     sig = -1 if x < 0 else 1
#     str_x = str(x * sig)
#     ans = int(str_x[::-1])
#     return ans * sig if ans < 2147483648 else 0


def reverse(x):
    sig = -1 if x < 0 else 1
    str_x = str(x*sig)
    l = len(str_x)
    r = str_x[::-1]
    if l > 10:
        return 0
    elif l == 10:
        i = 0
        maxInt = '2147483648'
        while i < l:
            print(r[i], maxInt[i])
            if r[i] > maxInt[i]:
                return 0
            i += 1
    ans = int(r)
    return ans*sig


print(reverse(-123))
print(reverse(2147483648))
print(reverse(2147483412))

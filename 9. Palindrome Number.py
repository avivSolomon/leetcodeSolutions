# def isPalindrome(x):
#     p = str(x)
#     i = 0
#     while i < ((len(p)-1) / 2):
#         if p[i] != p[-i-1]:
#             return False
#         i += 1
#     return True
#
# print(isPalindrome(12121))


def double_letter(my_str):
    temp = []
    for l in my_str:
        temp = temp + [''.join(l * 2)]
    return ''.join(temp)

print(double_letter("we are the champions!"))

st = """wwee  aarree  tthhee  cchhaammppiioonnss!!
wwee  aarree  tthhee  cchhaammppiioonnss!!"""
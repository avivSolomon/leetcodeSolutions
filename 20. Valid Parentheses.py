#
# def isValid(s):
#     close_brackets = '()[]{}'
#     brackets = []
#     for i in s:
#         if i in close_brackets[::2]:
#             brackets += i
#         if i in close_brackets[1::2]:
#             if (len(brackets) >= 1) and (close_brackets[close_brackets.index(i)-1] == brackets[-1]):
#                 brackets = brackets[:-1]
#             else:
#                 return False
#
#     if brackets == []:
#         return True
#
# print(isValid("a (cskah fkjd) jds{ [sj gd}] sk {xs}"))


def isValid(s):
    close = ')]}'
    brackets = []
    for i in s:
        brackets += i
        if i in close and len(brackets) > 1:
            if chr(ord(i) - 2 + 0 ** close.index(i)) == brackets[-2]:
                brackets = brackets[:-2]
            else:
                return False
    return True if len(brackets) == 0 else False


print(isValid("([])[]{}"))

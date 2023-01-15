
digits_letters = {"2": ["a",'b','c'], "3": ['d','e','f'], "4": ['g','h','i'], "5": ['j','k','l'], "6": ['m', 'n','o'],
                  "7": ['p','q','r','s'], "8": ['t','u','v'], "9": ['w','x','y','z']}

def letterCombinations(digits):
    """
    Returns a list of all possible letter combinations for a given list of digits.
    """
    n = len(digits)
    if n == 0:
        return ""
    combinations1 = [i for i in digits_letters[digits[0]]]
    if n == 1:
        return combinations1
    else:
        for num in digits[1:]:
            combinations3 = []
            for cher in digits_letters[num]:
                combinations2 = [com + cher for com in combinations1]
                combinations3 = combinations3 + combinations2
            combinations1 = combinations3
        return combinations3

def letterCombinations2(digits):
    letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    if digits == "":
        return ""
    combinations = letters[digits[0]]
    for num in digits[1:]:
        combinations = [old + new for old in combinations for new in letters[num]]
    return combinations

print(letterCombinations2("234"))
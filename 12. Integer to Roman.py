
def intToRoman(num: int) -> str:
	roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	digits_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	ans = ''
	for i in range(13):
		m = num//digits_val[i]
		ans += roman_digits[i] * m
		num %= digits_val[i]
	return ans

print(intToRoman(1994))

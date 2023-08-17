class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		dic = {ch: ransomNote.count(ch) for ch in set(ransomNote)}
		for k in dic.keys():
			if magazine.count(k) < dic[k]:
				return False
		return True

print(Solution().canConstruct("bg", "baa"))
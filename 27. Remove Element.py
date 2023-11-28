class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        x = [num for num in nums if num != val]
        l = len(x)
        nums[:l] = x
        print(nums)
        return l


    def removeElement2(self, nums: list[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        print(nums)
        return i

print(Solution().removeElement([3,2,2,3], 3))
print(Solution().removeElement2([3,2,2,3], 3))

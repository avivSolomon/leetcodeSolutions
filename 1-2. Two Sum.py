from typing import Optional


def twoSum(nums, target):
    i = 0
    while i < len(nums):
        if (target - nums[i]) in nums:
            return [i, nums[i+1:].index(target - nums[i]) + i]
        i += 1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, prev = l1, None
        carry = 0
        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            l1.val, carry = sum_ % 10, sum_ // 10
            prev, l1, l2 = l1, l1.next, l2.next

        if l2:
            prev.next, l1 = l2, l2

        while l1 and carry:
            sum_ = l1.val + carry
            l1.val, carry = sum_ % 10, sum_ // 10
            prev, l1 = l1, l1.next

        if carry:
            prev.next = ListNode(val=1)
        return head


l1 = ListNode(8)
l2 = ListNode(9)
l3 = ListNode(9)
l4 = ListNode(2)
# l5 = ListNode()
# l6 = ListNode()
l1.next = l2
l2.next = l3
# l4.next = l5
# l5.next = l6

print(Solution().addTwoNumbers(l1, l4))

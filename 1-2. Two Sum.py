

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


def addTwoNumbers(l1, l2):
    sum_l1_l2 = 0
    i = 0
    node = l1
    while node:
        sum_l1_l2 += node.val * (10 ** i)
        node = node.next
        i += 1

    i = 0
    node = l2
    while node:
        sum_l1_l2 += node.val * (10 ** i)
        node = node.next
        i += 1
    print(sum_l1_l2)

    node = ListNode()
    l3 = node
    i = 0
    j = len(str(sum_l1_l2))
    print(j)
    while i < j:
        node.val = sum_l1_l2 % 10
        sum_l1_l2 = sum_l1_l2 // 10
        print(node.val)
        i += 1
        if i < j:
            node.next = ListNode()
            node = node.next
        else:
            return l3


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

print(addTwoNumbers(l1, l4))


def threeSum(nums):
    # three_sum = []
    # i = 0
    # while i < len(nums) - 2:
    #     j = -1
    #     while len(nums[i+1:j]) > 0:
    #         if -(nums[i]+nums[j]) in nums[i+1:j] and sorted([nums[i], -(nums[i] + nums[j]), nums[j]]) not in three_sum:
    #             three_sum =three_sum + [sorted([nums[i], -(nums[i] + nums[j]), nums[j]])]
    #         j -= 1
    #     # print(sorted(three_sum))
    #     i += 1
    # return three_sum

    # three_sum = []
    # plus = sorted([p for p in nums if p > 0])
    # minus = sorted([m for m in nums if m < 0])
    # zero = len(nums) - len(plus) - len(minus)
    # if zero > 0:
    #     nzn = [[-n, 0, n] for n in set(plus) if -n in set(minus)]
    #     if zero > 2:
    #         nzn += [[0, 0, 0]]
    #     three_sum = three_sum + nzn
    # max_len = max(len(plus), len(minus))
    # i = 0
    # while i < max_len - 1:
    #     if i < len(plus) - 1:
    #         ppm = [[plus[i], p, -plus[i] - p] for p in set(plus[i+1:]) if (-plus[i] - p) in minus]
    #         three_sum = three_sum + ppm
    #     if i < len(minus) - 1:
    #         pmm = [[minus[i], m, -minus[i] - m] for m in set(minus[i+1:]) if (-minus[i] - m) in plus]
    #         three_sum = three_sum + pmm
    #     i += 1
    # return three_sum

    three_sum = []
    sort_num = sorted(nums)
    i = 0
    while i < len(sort_num):
        if sort_num[i] >= 0:
            minus = sort_num[:i]
            break
        i += 1
    set_minus = list(set(minus))

    plus = sort_num[len(minus):]
    i = 0
    while i < len(plus):
        if plus[i] != 0:
            zero = len(plus[:i])
            plus = plus[i:]
            set_plus = list(set(plus))
            break
        i += 1

    if zero > 0:
        nzn = [[-n, 0, n] for n in set_plus if -n in set_minus]
        if zero > 2:
            nzn += [[0, 0, 0]]
        three_sum = three_sum + nzn
    max_len = max(len(plus), len(minus))
    i = 0
    while i < max_len - 1:
        if i < len(plus) - 1:
            ppm = [[plus[i], p, -plus[i] - p] for p in set(plus[i+1:]) if (-plus[i] - p) in minus]
            three_sum = three_sum + ppm
        if i < len(minus) - 1:
            pmm = [[minus[i], m, -minus[i] - m] for m in set(minus[i+1:]) if (-minus[i] - m) in plus]
            three_sum = three_sum + pmm
        i += 1
    return three_sum


print(threeSum([-1,1,0,2,-1,0,-4,-2,-3,3,4,0]))


        ans = set([])
        minus, plus, zero = [], [], 0
        sort_num = sorted(nums)
        i = 0
        while i < len(sort_num):
            if sort_num[i] >= 0:
                minus = sort_num[:i]
                break
            i += 1
        minus_c = set(minus)

        plus = sort_num[len(minus):]
        i = 0
        while i < len(plus):
            if plus[i] != 0:
                zero = len(plus[:i])
                plus = plus[i:]
                break
        i += 1
        plus_c = set(plus)

        # all zero
        if zero>2:
            ans.add((0,0,0))
        # plus zero minus
        if zero>0:
            for n in minus:
                if -n in plus_c:
                    ans.add((n,0,-n))
        # plus minus minus
        n = len(minus)
        for i in range(n):
            for j in range(i+1,n):
                diff = -(minus[i]+minus[j])
                if diff in plus_c:
                    ans.add((minus[i],minus[j],diff))
        # plus plus minus
        n = len(plus)
        for i in range(n):
            for j in range(i+1,n):
                diff = -(plus[i]+plus[j])
                if diff in minus_c:
                    ans.add((diff,plus[i],plus[j]))
        return list(ans)
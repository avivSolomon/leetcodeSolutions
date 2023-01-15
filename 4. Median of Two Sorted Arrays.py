
def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    t = 0

    # Checking if one of the groups is really bigger than the other group
    if nums1[-1] <= nums2[0]:
        new = nums1 + nums2
    elif nums2[-1] <= nums1[0]:
        new = nums2 + nums1

    #
    else:
        if (n % 2 == 1) or (m % 2 == 1):
            if n % 2 == 1:
                x = nums1[n//2]
                if x >= nums2[m/2]:
                    for i in nums2[m/2:]:
                        if x >= i:
                            t += 1
                        else:
                            break
                else:
                    for i in nums2[-1:m / 2:-1]:
                        if x <= i:
                            t += 1
                        else:
                            break
            else:
                x = nums2[m // 2]
                if x >= nums1[n / 2]:
                    for i in nums1[n / 2:]:
                        if x >= i:
                            t += 1
                        else:
                            break
                else:
                    for i in nums1[-1:n / 2:-1]:
                        if x <= i:
                            t += 1
                        else:
                            break
        else:
            if n > m:
                start = nums1[:n / 2]
                end = nums1[n / 2:]
                if nums2[(m/2) - 1] >= end[0]:
                    for i in nums2[m/2:]:
                        if end[0] <= i:
                            t += 1
                        else:
                            break
                elif nums2[(m/2)] <= start[-1]:
                    for i in nums2[-1:m/2]:
                        if start[-1] <= i:
                            t += 1
                        else:
                            break
                else:
                    new = sorted(nums2[(m/2)-1] +nums2[(m/2)] +start[-1] + end[0])
                    return (new[1]+new[2])/2
            else:
                start = nums2[:m / 2]
                end = nums2[m / 2:]


    # middle = []
    # new_len = 0
    #
    # len1 = len(nums1)
    # if len1 > 2:
    #     if len1 % 2 == 0:
    #         middle1 = nums1[(len1 // 2) - 1: (len1 // 2) + 1]
    #         t1 = nums1[(len1 // 2) - 3: (len1 // 2) + 3]
    #         new_len += 2
    #     else:
    #         middle1 = [nums1[len1 // 2]]
    #         new_len += 1
    # else:
    #     middle1 = nums1
    #     new_len += len1
    #
    # len2 = len(nums2)
    # if len2 > 2:
    #     if len1 % 2 == 0:
    #         middle2 = nums2[(len2 // 2) - 1: (len2 // 2) + 1]
    #         new_len += 2
    #     else:
    #         middle2 = [nums2[len2 // 2]]
    #         new_len += 1
    # else:
    #     new_len += len2
    #     middle2 = nums2
    #
    # if middle1[-1] <= middle2[0]:
    #     if middle1[-1] <= :
    #
    # print(middle)
    #
    # if new_len % 2 == 0:
    #     av = sum(middle[(new_len // 2) - 1: (new_len // 2) + 1]) / 2
    # else:
    #     av = middle[(new_len // 2)]
    # return av


print(findMedianSortedArrays([1,2,3,4,5],[3,4,6,7,8,9]))

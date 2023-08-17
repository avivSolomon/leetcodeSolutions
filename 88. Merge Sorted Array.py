
def merge(nums1: [list[int]], m: int, nums2: [list[int]], n: int) -> None:
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	i, j = 0, 0
	nums1[:], nums2[:] = nums1[:m], nums2[:n]
	nums = []
	while i < m and j < n:
		if nums1[i] < nums2[j]:
			nums.append(nums1[i])
			i += 1
		else:
			nums.insert(nums2[j])
			j += 1
	nums += nums1[i:] + nums2[j:]
	nums1[:] = nums
	print(nums)


merge([1,2,3,0,0,0], 3, [2,5,6], 3)

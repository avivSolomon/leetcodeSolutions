
def maxArea(height):
    first = 0
    last = len(height) - 1
    max_area = 0

    while first < last:
        max_area = max(min(height[last], height[first]) * (last - first), max_area)
        if height[last] < height[first]:
            last -= 1
        else: first += 1
    return max_area


# print(maxArea([7,8,6,2,5,4,8,3,5]))
# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,2,1]))
print(maxArea([2,3,10,5,7,8,9]))


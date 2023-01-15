
def jump(nums):
    x = len(nums) - 1
    step = 0
    while x:
        i = 0
        while i < x:
            if i + nums[i] >= x:
                x = i
            i += 1
        step += 1
    return step

def jump2(nums):
    x = len(nums) - 1
    step = 0
    i = 0
    while i < x:
        j = nums[i]
        if i +j >= x:
            next_nums = nums[i+1:]
            step += 1
            break
        else:
            next_nums = nums[i+1:i+j+1]

        next_step = [a + next_nums[a] for a in range(j)]
        jump_len = next_step.index(max(next_step)) + 1
        i += jump_len
        step += 1
    return step

print(jump2([1,2,3,1,4,5]))


y=4567
z=0
while y:
    z += z*9 + y%10
    y = y//10
print(z)
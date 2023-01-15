from math import comb

def climbStairs(n):
    min_step = (n % 2) + (n // 2)
    com_step, num_step = 0, min_step
    while num_step <= n:
        com_step += comb(num_step, n - num_step)
        num_step += 1
    return com_step

print(climbStairs(6))

def climbStairs2(n):
    i, com_step = 0, []
    while i <= n:
        if i <= 3:
            com_step = com_step + [i]
        else:
            com_step = com_step + [com_step[i-1] + com_step[i-2]]
        i += 1
    return com_step[-1]

print(climbStairs2(7))


def fibo_recu(an):
    if an <= 3:
        return an
    return fibo_recu(an-1) + fibo_recu(an-2)

print(fibo_recu(4))


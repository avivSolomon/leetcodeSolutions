import math

def max_distance(number):
    index_bit = []
    print("Binary representation:", bin(number)[2:])

    num_bit = bin(number)[2:]
    count = 0
    temp = 0
    for num in num_bit:
        if num == '1':
            index_bit = index_bit + [count]
            if len(index_bit) > 1:
                dis = index_bit[-1] - index_bit[-2] - 1
                if dis > temp:
                    temp = dis
        count += 1
    print(index_bit)

    print(temp)

print('the greatest distance:', max_distance(int(input('Enter your number:'))))
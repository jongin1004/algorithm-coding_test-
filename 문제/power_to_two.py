n = int(input())
# result = False

# if n == 1 :
#     result = True

# else :
#     for i in range(-31, 32):
#         if 2 ** i == n:
#             result = True

# print(result)


def power_to_two(n) :
    if n == 1 :
        return True
    temp = 1
    while(True) :
        if temp >= n :
            return temp == n
        else :
            temp *= 2

print(power_to_two(n))

    
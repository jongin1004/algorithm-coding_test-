input_list = [1, 2, 1, 2, 4]
count_list = [0] * (len(input_list) + 1)

for num in input_list:
    count_list[num] += 1

result = count_list.index(1)

print(result)
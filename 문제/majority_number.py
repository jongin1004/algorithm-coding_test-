input_list = [1, 2, 1, 1, 2]
count_list = [0] * (len(input_list) + 1)

for num in input_list:
    count_list[num] += 1

result = count_list.index(max(count_list))
print(result)


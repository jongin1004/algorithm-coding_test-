input_list = [1, 3, 5, 6, 7, 10]
target = 12
idx = 0

for i in range(len(input_list)) :
    if target <= input_list[i] :
        idx = i
        break

    idx = len(input_list)

print(idx)

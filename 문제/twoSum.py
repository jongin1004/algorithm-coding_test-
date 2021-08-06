num_arr = [2, 7, 11, 15]
target = 9

for i in range(len(num_arr)):
    for j in range(i + 1, len(num_arr)):
        if num_arr[i] + num_arr[j] == target:
            print(i, j)
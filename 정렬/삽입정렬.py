arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 4, 5, 8, 12]

for i in range(1, len(arr)) :
    min_idx = i
    for j in range(i, 0, -1) :        
        if arr[min_idx] < arr[j-1] :            
            arr[j-1], arr[min_idx] = arr[min_idx], arr[j-1]
            min_idx = j-1

print(arr)

            
#========================================\
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else :
            break

print(arr)
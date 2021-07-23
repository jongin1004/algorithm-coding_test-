def binary_search(arr, search, start, end) :
    if start >= end :        
        return None

    middle = (end + start) // 2

    if arr[middle] > search :
        return binary_search(arr, search, start, middle - 1)
    elif arr[middle] < search :
        return binary_search(arr, search, middle + 1, end)
    else :
        return middle
    # if arr[middle] == search :
    #     return middle
    # elif arr[middle] > search :
    #     return binary_search(arr, search, start, middle - 1)
    # else :
    #     return binary_search(arr, search, middle + 1, end)


n, search = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, search, 0, n - 1)

if result == None :
    print("원소가 존재하지 않습니다.")

else :
    print(result + 1)
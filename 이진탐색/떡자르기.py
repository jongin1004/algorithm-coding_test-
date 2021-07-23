# def binary_search(arr, goal, start, end) :
#     if start > end :
#         return 

#     middle = (start + end) // 2
#     rest = 0
#     for length in arr :
#         rest += (length - middle) 

#     if rest == goal :
#         return middle
#     elif rest > goal :
#         return binary_search(arr, goal, middle + 1, end) 
#     else :
#         return binary_search(arr, goal, start, middle - 1)
        

    
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
start = 0
end = max(arr)

while(start <= end) :
    rest = 0
    middle = (start+end) // 2
    for length in arr :
        if length > middle :
            rest += length - middle
    
    if rest < m :
        end = middle - 1

    else :
        result = middle
        start = middle + 1

print(result)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quik(arr, start, end) :
    if len(arr) <= 1 :
        return 

    pivot = arr[start]
    pivot_plus = 0
    pivot_minus = 0 

    
    while True :
        for i in range(start+1, end+1) :
            if arr[i] > pivot :        
                pivot_plus = i
                break
        
        for j in range(end, start, -1) :
            if arr[j] < pivot :        
                pivot_minus = j
                break

        if pivot_plus >= pivot_minus :
            arr[start], arr[pivot_minus], = arr[pivot_minus], arr[start]           
            break
            

        else :
            arr[pivot_plus], arr[pivot_minus] = arr[pivot_minus], arr[pivot_plus]

    quik(arr, start, pivot_minus - 1)
    quik(arr, pivot_minus + 1, end)


quik(arr, 0, len(arr)-1)
print(arr)



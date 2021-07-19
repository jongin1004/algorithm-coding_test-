import time

start_time = time.time() 

N, K = map(int, input().split(" "))
count = 0

while True :
    if N < K :
        break

    target = (N // K) * K
    count += (N - target)
    N = target

    count += 1
    N //= K

count += (N - 1)
print(count)
    
end_time = time.time() 
print("time : ", end_time - start_time)
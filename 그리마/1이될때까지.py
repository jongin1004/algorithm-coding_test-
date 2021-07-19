import time 
start_time = time.time()

N, K = map(int, input().split(" "))
count = 0

while N != 1 :
    if N % K != 0 :
        N -= 1
        count += 1

    else :
        N /= K
        count += 1

print(count)

end_time = time.time()
print("time : ", end_time - start_time)

people_number = int(input())
panic_value = list(map(int, input().split(" ")))
panic_value.sort()
N = 0
P = 0
count = 0

for i in panic_value :
    if i > P :
        P = i 

    N += 1

    if N >= P :
        count += 1
        P = 0
        N = 0

print(count)

#_---------------------------
#굳이 패닉값을 담아둘 변수를 만들 필요없이 i로 처리하면 더 짧아진다.
#오름차순으로 정렬했기 때문에, i값만으로도 가능함. 
for i in panic_value :
    N += 1

    if N >= i :
        count += 1        
        N = 0

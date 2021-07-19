position = input()
x = int(position[1])
y = ord(position[0])-ord("a") + 1
count = 0
route = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2)]

for i in route : 
    nx = x + i[0]
    ny = y + i[1]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8 :
        continue

    count += 1

print(count)

N = int(input())
route = input().split(" ")
X, Y = 1, 1

direction_coordinate = [(0, 1), (0, -1), (1, 0), (-1, 0)]
move_types = ["R", "L", "D", "U"]

for i in route :
    way = move_types.index(i)    
    nx = X + direction_coordinate[way][0]
    ny = Y + direction_coordinate[way][1]

    if nx >= 1 and nx < N+1 and ny >= 1 and ny < N+1 :
        X, Y = nx, ny

print(X, Y)

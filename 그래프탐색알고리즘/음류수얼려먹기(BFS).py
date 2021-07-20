from collections import deque

def bfs(i, j) :    
    if graph[i][j] != 0 :
        return False

    queue = deque([(i, j)])
    graph[i][j] = 1

    while queue :
        x, y = queue[0][0], queue[0][1]
        queue.popleft()
        for path in path_arr :
            i = x + path[0]
            j = y + path[1]
            if i <= -1 or i >= n or j <= -1 or j >= m :                
                continue
            
            if graph[i][j] != 0 :                
                continue
            graph[i][j] = 1
            queue.append((i, j))            
    return True


n, m = map(int, input().split())
result = 0
graph = []

for i in range(n) :
    graph.append(list(map(int, input())))

path_arr = [(0, 1), (0, -1), (1, 0) ,(-1, 0)]

for i in range(n) :
    for j in range(m) :
        if bfs(i, j) == True :
            result += 1

print(result)
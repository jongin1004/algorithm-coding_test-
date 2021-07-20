from collections import deque

def bfs(x, y) :
    queue = deque([(x, y)])

    while queue:
        x, y = queue[0][0], queue[0][1]        
        queue.popleft()
        for path in path_arr :
            i = x + path[0]
            j = y + path[1]
            if i <= -1 or i >= n or j <= -1 or j >= m :
                continue

            if graph[i][j] == 0 :
                continue

            
            graph[i][j] = graph[x][y] + 1
            queue.append((i, j))

        if x == n-1 and y == m-1 :
            return
        graph[x][y] = 0
        
n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))
path_arr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

bfs(0, 0)
print(graph[n-1][m-1])

# =================================================

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for path in path_arr :
            i = x + path[0]
            j = y + path[1]
            if i <= -1 or i >= n or j <= -1 or j >= m :
                continue

            if graph[i][j] == 0 :
                continue

            if graph[i][j] == 1 :
                graph[i][j] = graph[x][y] + 1
                queue.append((i, j))
    
    return graph[n - 1][m - 1]
        
n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

#이동할 네가지 방향
path_arr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

print(bfs(0, 0))
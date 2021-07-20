# from collections import deque

# n = int(input())
# arr = []

# for i in range(n) :
#     arr.append(input())

# visited = [[False] * len(arr[0]) for _ in range(n)]
# coordinate = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# bfs(arr, 0, 0, visited)

# def bfs(arr, x, y, visited) :
#     if arr[x][y] == "0" :
#         queue = deque([x, y])
        
#     visited[x][y] = True

#     while queue :hfllhfdlhhrr ad sada yubA
#         v = queue.popleft()

#         for i in coordinate :
#             nx, ny= x+i[0], y+i[1]
#             if nx >= 0 and nx < n and ny >= 0 and ny < len(arr[0]) and :

#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        #상, 하, 좌, 우의 위치들도 모두 재귀적을 ㅗ호출
        dfs(x - 1, y)
        dfs(x , y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False
n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
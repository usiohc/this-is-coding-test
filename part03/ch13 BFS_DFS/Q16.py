# 연구소 - 백준 14502번

import copy
from collections import deque

def bfs():
    queue = deque()
    aftergraph = copy.deepcopy(graph)

    for v in virus:
        queue.append(v)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if aftergraph[nx][ny] == 0:
                aftergraph[nx][ny] = 2
                queue.append((nx, ny))

    global result
    tmp = 0
    for rows in aftergraph:
        tmp += rows.count(0)

    result = max(result, tmp)


def count(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(n)]
virus = [(i, j) for j in range(m) for i in range(n) if graph[i][j] == 2]

result = 0
count(0)
print(result)
# second solution

from collections import deque 

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(q):
    while q:
        v, y, x, cnt = q.popleft()

        if cnt == s:
            return

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if 0>ny or ny>=n or 0>nx or nx>=n:
                continue

            if board[ny][nx] == 0:
                board[ny][nx] = v
                q.append((v, ny, nx, cnt+1))


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, a, b = map(int, input().split())

que = []
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            que.append((board[i][j], i, j, 0))

solution(deque(sorted(que)))
# print(*board, sep='\n')
print(board[a-1][b-1])

# --------------
# first solution

# from collections import deque 

# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# def solution(que):
#     while que:
#         y, x = que.popleft()

#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]

#             if 0>ny or ny>=n or 0>nx or nx>=n or visited[ny][nx]:
#                 continue

#             if board[ny][nx] == 0:
#                 board[ny][nx] = board[y][x]
#             elif board[ny][nx] > 0:
#                 board[ny][nx] = min(board[ny][nx], board[y][x])
                
                


# n, k = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]
# s, a, b = map(int, input().split())


# for _ in range(s):
#     que = deque()
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j] and board[i][j]>0:
#                 que.append((i, j))
#                 visited[i][j] = True
#     solution(que)
#     if visited[a-1][b-1] or board[a-1][b-1]>0:
#         break

# print(board[a-1][b-1])
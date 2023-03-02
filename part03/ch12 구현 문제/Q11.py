# 뱀 - 백준 3190번
# 전체적인 흐름은 완성했는데 세부적인 구현에서 오래걸렸음


from collections import deque

n = int(input())
k = int(input())
array = [[0]*n for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    array[x-1][y-1] = 1

# 방향
# R D L U = 0 1 2 3
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = 0
snakes = deque()
snakes.append((0, 0))
x, y = 0, 0

l = int(input())
d_lst = []
for _ in range(l):
    c, ld = input().split()
    d_lst.append((int(c), ld))
d_lst.append((10001, _))



Flag = False
cnt = 0
for i in range(l+1):
    c, ld = d_lst[i] 
    while cnt<c:
        nx, ny = x+dx[d], y+dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=n or ((nx, ny) in snakes):
            cnt += 1
            Flag = True
            break
        
        if array[ny][nx] == 1:
            array[ny][nx] = 0
            snakes.append((nx, ny))
        else:
            snakes.popleft()
            snakes.append((nx, ny))

        x, y = nx, ny
        cnt += 1

    if ld == 'D':
        d = (d+1)%4
    elif ld == 'L':
        d = (d+3)%4

    if Flag:
        break


print(cnt)


n, m = map(int, input().split())
x, y, direction = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
cntmap = [[0] * m for _ in range(n)]
cntmap[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 방문한적? and 육지인지?
    if cntmap[nx][ny] == 0 and map[nx][ny] == 0:
        cntmap[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        
        turn_time = 0

print(cnt)
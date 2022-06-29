# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# best solution

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# my solution

# n = int(input())
# start = [1, 1]

# commands = list(input().split())

# for cmd in commands:

#     if cmd == 'L':
#         start[1] -= 1
#     elif cmd == 'R':
#         start[1] += 1
#     elif cmd == 'U':
#         start[0] -= 1
#     elif cmd == 'D':
#         start[0] += 1
    
#     if start[0] == 0 or start[0] == n+1:
#         start[0] = abs(start[0] - 1)
#     if start[1] == 0 or start[1] == n+1:
#         start[1] = abs(start[1] - 1)

# print(*start, sep=' ')

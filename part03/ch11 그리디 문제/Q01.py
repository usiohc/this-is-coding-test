# 모험가 길드

n = int(input())
fears = sorted(list(map(int, input().split())), reverse=True)
last_fear = 0
cnt = 0
result = 0

for f in fears:
    if cnt == 0:
        last_fear = f
    cnt += 1

    if cnt >= last_fear:
        result += 1
        cnt = 0

print(result)

'''
input
5
2 3 1 2 2

output
2

input
7
1 1 1 1 1 1 1

output
7

input
10
1 2 3 4 5 6 7 8 9 10

output
1

input
6
4 3 3 3 3 2

output
1
'''
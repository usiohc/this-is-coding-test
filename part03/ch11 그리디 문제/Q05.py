# 볼링공 고르기
'''
2명이 하나씩 고르는 조합? -> 조합 combinations
'''
from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))
cnt = 0

for a, b in combinations(balls, 2):
    if a != b:
        cnt += 1
print(cnt)

# sol_2는 답안 예시
'''
그냥 모범 답안 정도 인듯
볼링공의 개수를 1부터 m까지 n에서 빼가면서
남아있는 볼링 공의 개수와 현재 볼링공의 개수를 곱해 경우의 수를 정답에 더하는 방식
'''

def sol_2():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    array = [0] * 11

    for x in data:
        array[x] += 1

    result = 0
    for i in range(1, m+1):
        n -= array[i]
        result += array[i] * n
    print(result)

'''
input
5 3
1 3 2 3 2
output
8

input
8 5
1 5 4 3 2 4 5 2
output
25
'''
# 치킨 배달 - 백준 15686번
import sys
from itertools import combinations
input = sys.stdin.readline

def solution(n, m):
    houses, comb = [], []

    for i in range(n):
        ip = list(map(int, input().split()))
        for j in range(n):
            if ip[j] == 2:
                comb.append((i, j))
            elif ip[j] == 1:
                houses.append((i, j))
    
    result = 1e4
    for cb in combinations(comb, m):
        dist = 0
        # print(cb)
        for x, y in houses:
            d = 1e4
            for xx, yy in cb:
                d = min(d, abs(xx-x)+abs(yy-y))
            dist += d
        result = min(result, dist)
    return result


N, M = map(int, input().split())
print(solution(N, M))
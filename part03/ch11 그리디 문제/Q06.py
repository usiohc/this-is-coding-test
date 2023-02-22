# 무지의 먹방 라이브 - 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/42891)
# k의 최대가 2*10**13 그대로 접근하면 당연히 시간초과

# min 만큼은 돌아야 [i] 위치에 0이 생기면서 그리디가 필요한 시점?
# -> heapq 우선순위 큐로 남은 음식시간을 우선순위로 잡아보자

import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    heap = []
    for i in range(n):
        heapq.heappush(heap, (food_times[i], i+1))

    l_cost = 0
    while heap:
        if (heap[0][0]-l_cost)*n > k:
            heap.sort(key= lambda x:x[1])
            return heap[k%n][1]
        else:
            ft = heapq.heappop(heap)
            k -= (ft[0] - l_cost) * n
            l_cost = ft[0]
            n -= 1 

    return -1

print(solution([3, 1, 2], 5))
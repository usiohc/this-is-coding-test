from collections import deque

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
cost = [0] * (n+1)

for i in range(1, n+1):
    line = list(map(int, input().rstrip('-1').split()))
    cost[i] = line.pop(0)
    for l in line:
        graph[l].append(i)
        indegree[i] += 1

print(graph, indegree)

def topology_sort():
    result = cost[:]
    que = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
    
    while que:
        q = que.popleft()

        for i in graph[q]:
            indegree[i] -= 1
            result[i] = max(result[i], result[q]+cost[i])
            if indegree[i] == 0:
                que.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()

# input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
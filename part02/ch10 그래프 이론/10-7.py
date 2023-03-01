import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# o == 1
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# o == 0
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [i for i in range(n+1)]


for _ in range(m):
    o, a, b = map(int, input().split())
    
    # find 1
    if o:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
    # union 0
    else:
        union_parent(parent, a, b)

# 7 8
# 0 1 3
# 1 1 7
# NO
# 0 7 6
# 1 7 1
# NO
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
# YES
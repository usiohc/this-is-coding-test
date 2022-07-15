n = int(input())

array = []
for _ in range(n):
    tmp = input().split()
    array.append((tmp[0], int(tmp[1])))

array.sort(key= lambda x:x[1])

for s in array:
    print(s[0], end=' ')
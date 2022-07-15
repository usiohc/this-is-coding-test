# 문제 해설 소스

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))


# 내가 푼 소스

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
result = sum(a)
for _ in range(k):
    a.append(max(b))
    a.remove(min(a))
    b.remove(max(b))
    
    cnt += 1
    tmp = sum(a)
    if result >= tmp:
        cnt -= 1
        break

    result = tmp

print(cnt, result)

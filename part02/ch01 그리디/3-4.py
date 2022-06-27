n, k = map(int, input().split())
result = 0

while n >= k:
    if n%k == 0:
        n //= k
        result += 1
    else:
        tmp = n%k
        n -= tmp
        result += tmp
    # print(n, result)


while n != 1:
    n -= 1
    result += 1

print(result)
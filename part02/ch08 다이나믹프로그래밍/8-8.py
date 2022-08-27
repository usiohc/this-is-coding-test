# 효율적인 화폐구성

n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]

dp = [10001] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(moneys[i], m+1):
        if dp[j - moneys[i]] != 10001:
            dp[j] = min(dp[j], dp[j - moneys[i]] + 1)
        
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
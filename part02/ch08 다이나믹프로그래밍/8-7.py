# 바닥 공사

n = int(input())
dp = [0] * (n+1)

# 1 * 2
dp[1] = 1
# 2 * 2
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796

print(dp[n])
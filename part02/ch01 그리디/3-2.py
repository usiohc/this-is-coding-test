# 단순하게 문제를 푸는 방법
# 그냥 문제를 코드로 표현한 것임

# n, m ,k = map(int, input().split())

# data = list(map(int, input().split()))
# data.sort()
# first = data[n-1]
# second = data[n-1]

# result = 0

# while True:
#     for i in range(k):
#         if m==0:
#             break
#         result += first
#         m -= 1
#     if m==0:
#         break
#     result += second
#     m -= 1

# print(result)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ   
# 반복되는 수열을 찾아서 푼 코드

n, m ,k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/ (k+1)) * k 
count += m%(k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
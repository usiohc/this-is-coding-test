# 곱하기 혹은 더하기

n = list(map(int, input()))
result = n[0]
for i in range(1, len(n)):
    result = max(result*n[i], result+n[i])
print(result)

'''
input
02984
output
576

input
567
output
210
'''
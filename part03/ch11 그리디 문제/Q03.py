# 문자열 뒤집기
# 백준 1439번
s = list(map(int, input()))

lst = [s[0]]

for i in range(1, len(s)):
    if lst[-1] != s[i]:
        lst.append(s[i])
print(lst)
if len(lst)==1:
    print(0)
else:
    print(min(lst.count(1), lst.count(0)))

'''
input
0001100
output
1


input
01100000
output
1

input
01101000
output
2


'''

# 럭키 스트레이트 - 백준 18406번

n = list(map(int, input()))
l, r = n[:len(n)//2],n[len(n)//2:]
if  sum(l) == sum(r):
    print('LUCKY')
else:
    print('READY')
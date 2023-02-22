# 문자열 재정렬

n = sorted(list(input()))
for i in range(len(n)):
    if not n[i].isnumeric():
        # print(''.join(n[i:]) + str(sum(map(int, n[:i]))))
        print(*n[i:],sum(map(int, n[:i])), sep='')
        break
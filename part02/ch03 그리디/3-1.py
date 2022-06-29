n = 1260
cnt = 0

moneys = [500, 100, 50, 10]

for money in moneys:
    cnt += n // money
    n %= money

print(cnt)
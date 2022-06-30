knight = input()
row = int(knight[-1])
column = int(ord(knight[0])) - ord('a') + 1

steps = [(-2, -1), (-1, -2), 
         (2, -1), (1, -2),
         (-2, 1), (-1, 2), 
         (2, 1), (1, 2)]
cnt = 0

for step in steps:
    x = row + step[0]
    y = column + step[1]
    if x>=1 and x<=8 and y>=1 and y<=8:
        cnt += 1

print(cnt)
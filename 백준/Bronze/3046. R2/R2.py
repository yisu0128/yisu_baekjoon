rs = input().split()
r1 = int(rs[0])
s = int(rs[1])

for r2 in range(-1000, 1001):
    if s == (r1+r2)/2:
        print(r2)

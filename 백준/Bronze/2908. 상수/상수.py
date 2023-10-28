a,b = map(str, input().split())
a0 = a[2]
a1 = a[1]
a2 = a[0]
a = a0+a1+a2

b0 = b[2]
b1 = b[1]
b2 = b[0]
b = b0+b1+b2

if int(a) >= int(b):
    print(a)
else:
    print(b)
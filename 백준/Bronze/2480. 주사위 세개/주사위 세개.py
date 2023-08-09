n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
a < 7 and b <7 and c< 7
if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+b*100)    
elif a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    if a>b and a>c:
        print(a*100)
    elif b>c and  b>a:
        print(b*100)
    elif c>b and c>a:
        print(c*100)
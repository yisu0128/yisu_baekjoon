import sys

while True:
    try: 
        n = input().split()
        a= int(n[0])
        b = int(n[1])
        print(a+b)
    except:
        break
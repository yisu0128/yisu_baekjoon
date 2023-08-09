n = input().split()
H = int(n[0])
M = int(n[1])

if H >=1 :
    if M < 45:
        H = H-1
        M = 60-(45-M)
        print(H, M)
    elif M >= 45:
        M = M-45
        print(H,M)

else:
    
    if M < 45:
        H=24-1
        M = 60-(45-M)
        print(H, M)
    elif M >= 45:
        M = M-45
        print(H,M)
    

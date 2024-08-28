n = int(input())

def standing_tri(n):
    for i in range(1,n+1):
        print(" "*(n-i), end="")
        print("*"*i)
    for j in range(n-1,0,-1):
        print(" "*(n-j), end="")
        print("*"*j)


standing_tri(n)
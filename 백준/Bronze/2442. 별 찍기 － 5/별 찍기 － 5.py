n = int(input().strip())

def star_tree(n):
    for i in range(0,n):
        print(" "*(n-i-1), end ="")
        print("*"*(i+1), end ="")
        print("*"*i)

star_tree(n)
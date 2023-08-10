import sys


T = a = int(sys.stdin.readline())

for i in range(1, T+1):
    N1, N2 = map(int,sys.stdin.readline().split())
    
    print(N1+N2)
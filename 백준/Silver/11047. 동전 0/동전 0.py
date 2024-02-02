import sys 

input = sys.stdin.readline

n,k = map(int, input().split())

coins = list()
count = 0

for _ in range (n):
    coins.append(int(input()))
    coins.sort(reverse=True)

for i in range(n):
    if coins[i] > k:
        i+=1
    else: 
        count+=k//coins[i]
        k = k%coins[i]
        i+=1

print(count)
import sys

input = sys.stdin.readline
count = 0 
date = int(input())
car_plates = list(map(int, input().split()))

for i in car_plates:
    if i == date:
        count +=1

print(count)


import sys

input = sys.stdin.readline
numbers = list()
sum = 0
mena = list()

for i in range (7):
    no = int(input())
    numbers.append(no)

for number in numbers: 
    if number%2 ==1:
        sum += number
        mena.append(number)

if len(mena)==0:
    print(-1)

else:
    print(sum)
    print(min(mena))
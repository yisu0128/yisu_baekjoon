voca = str(input())
b = 0

for i in range(0, len(voca)//2):
    if voca[i] != voca[len(voca) - i - 1]:
        b = 1
        break

if b == 0:
    print(1)
else:
    print(0)

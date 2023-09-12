class1 = []
for _ in range(28):
    n = int(input())
    class1.append(n)

for i in range(1, 31):
    if i not in class1:
        print(i)
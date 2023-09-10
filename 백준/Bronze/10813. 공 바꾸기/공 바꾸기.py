n, m = map(int, input().split())
basket = [1]
for z in range(2, n+1):
    basket.append(z)


for y in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for _ in range(n):
    print(basket[_], end=' ')

n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
newscore = []
for _ in range(n):
    newscore.append(scores[_]/m*100)
print(sum(newscore)/n)

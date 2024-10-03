import sys
def can_reach_destination(test_cases):
    results = []
    for x, y, t in test_cases:
        distance = abs(x) + abs(y)
        
        if distance <= t and (t - distance) % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

num_cases = int(sys.stdin.readline().strip())
test_cases = []
for _ in range(num_cases):
    x, y, t = map(int, sys.stdin.readline().strip().split())
    test_cases.append((x, y, t))

results = can_reach_destination(test_cases)
for result in results:
    print(result)

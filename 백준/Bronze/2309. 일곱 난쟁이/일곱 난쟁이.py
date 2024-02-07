import sys

input = sys.stdin.readline

heights = list()
for _ in range(9):
    heights.append(int(input()))

heights.sort()

removed = False

for i in range(8):
    if removed:
        break
    for j in range(i + 1, 9):  # Fix the range here
        if sum(heights) - (heights[i] + heights[j]) == 100:
            heights.pop(j)
            heights.pop(i)
            removed = True
            break

for n in heights:
    print(n)


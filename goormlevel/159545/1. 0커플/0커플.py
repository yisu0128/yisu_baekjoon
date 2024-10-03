# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys 
count = 0
n = int(sys.stdin.readline().rstrip())
mlist = list(map(int,sys.stdin.readline().rstrip().split()))
unique_values = set(mlist)
for i in list(unique_values):  # 중복 제거된 리스트를 순회
    if -i in unique_values:
        unique_values.remove(i)   # 양수 제거
        unique_values.remove(-i)  # 음수 제거

# 남은 값들의 합을 구하기
print(sum(unique_values))

from collections import *

def solution(arr):
    arr2 = deque()
    arr2.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr2.append(arr[i])
    return list(arr2)
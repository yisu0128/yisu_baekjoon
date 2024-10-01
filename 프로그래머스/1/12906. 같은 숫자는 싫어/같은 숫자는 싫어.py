from collections import * 

def solution(arr):
    fl = list()
    fl.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] !=arr[i-1]:
            fl.append(arr[i])
    
    return fl
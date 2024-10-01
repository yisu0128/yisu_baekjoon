from collections import *
def solution(nums):
    print(nums)
    count = len(set(nums))
    if count > len(nums)/2:
        answer = len(nums)/2
    else: 
        answer = count
    return answer
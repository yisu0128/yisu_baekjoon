from collections import *
def solution(clothes):
    answer = 1
    clothes_counter = Counter([kind for name, kind in clothes])
    for count in clothes_counter.values():
        answer *= (count+1)
    return answer-1
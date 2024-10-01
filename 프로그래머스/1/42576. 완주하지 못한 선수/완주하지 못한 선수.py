from collections import *
def solution(participant, completion):
    answers = list(Counter(participant)-Counter(completion))
    answer = answers[0]
    return answer
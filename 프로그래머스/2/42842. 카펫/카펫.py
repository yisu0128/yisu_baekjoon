def solution(brown, yellow):
    answer = []
    for i in range(brown):
        for j in range(brown):
            if brown+yellow == i*j and (i-2)*(j-2)==yellow and i>=j:
                answer.append(i)
                answer.append(j)
                
    return answer
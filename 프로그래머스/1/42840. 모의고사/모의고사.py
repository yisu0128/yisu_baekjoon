def solution(answers):
    answer = []
    a = [1,2,3,4,5]*10000
    b = [2,1,2,3,2,4,2,5]*10000
    c = [3,3,1,1,2,2,4,4,5,5]*10000
    counta = 0
    countb =0
    countc = 0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            counta+=1
        if answers[i] == b[i]:
            countb+=1
        if answers[i] == c[i]:
            countc +=1
    if max(counta, countb, countc) == counta:
        answer.append(1),
    if max(counta, countb, countc) == countb:
        answer.append(2)
    if max(counta, countb, countc) == countc:
        answer.append(3)
        
    return answer
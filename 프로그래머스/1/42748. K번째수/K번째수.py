def solution(array, commands):
    answer = list()
    for i in range (len(commands)):
        newarr = array[commands[i][0]-1:commands[i][1]]
        newarr.sort()
        answer.append(newarr[commands[i][2]-1])
    return answer


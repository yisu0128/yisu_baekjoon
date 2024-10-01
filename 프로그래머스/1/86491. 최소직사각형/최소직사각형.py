def solution(sizes):
    answer = 0
    short = list()
    long = list()
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1]= sizes[i][1],sizes[i][0]
            short.append(sizes[i][0])
            long.append(sizes[i][1])
        else:
            short.append(sizes[i][0])
            long.append(sizes[i][1])
            
    return max(short)*max(long)
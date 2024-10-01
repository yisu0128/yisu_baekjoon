import math

def solution(progresses, speeds):
    answer = []
    days = list()

    # 각 작업이 완료되는 데 걸리는 날짜 계산
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # 첫 번째 작업의 기준 날짜
    front = days[0]
    count = 1

    # 두 번째 작업부터 비교하면서 배포 기준에 맞는 작업 묶음 계산
    for j in range(1, len(days)):
        if front >= days[j]:
            count += 1  # 배포 가능 그룹에 포함
        else:
            answer.append(count)  # 이전 그룹 배포
            count = 1  # 새로운 그룹 시작
            front = days[j]  # 기준을 현재 작업으로 변경
    
    answer.append(count)  # 마지막 남은 그룹 배포
    return answer

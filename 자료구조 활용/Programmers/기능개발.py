import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days = deque()
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) / speed
        day = math.ceil(day)
        days.append(day)
    print(days)

    while days:
        for i in range(len(days)):
            if days[i] == 0:
                continue
            days[i] -= 1

        if days and days[0] == 0:
            cnt = 0
            flag = True
            while flag and days:
                if days[0] == 0:
                    days.popleft()
                    cnt += 1
                else:
                    flag = False
            answer.append(cnt)

    print(answer)
    return answer
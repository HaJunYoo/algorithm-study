from collections import deque
import math


def ceil(num):
    if num - int(num) > 0:
        return int(num + 1)
    else:
        return int(num)

def solution(progresses, speeds):
    days = deque()
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) / speed

        days.append(ceil(num=day))

    print(days)
    answer = []
    f = 0
    while days:
        cnt = 0
        while True:
            if days:
                if days[0] <= f:
                    days.popleft()
                    cnt += 1
                else:
                    break
            else:
                break
        if cnt > 0:
            answer.append(cnt)
        f += 1

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))


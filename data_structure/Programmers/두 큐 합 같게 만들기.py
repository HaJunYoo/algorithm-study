from collections import deque


def solution(queue1, queue2):
    answer = -1
    qsize = len(queue1)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)

    for i in range(0, 4 * qsize):
        answer += 1
        if q1_sum == q2_sum:
            return answer
        elif q1_sum < q2_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            q1_sum += tmp
            q2_sum -= tmp
        else:
            tmp = q1.popleft()
            q2.append(tmp)
            q1_sum -= tmp
            q2_sum += tmp

    return -1
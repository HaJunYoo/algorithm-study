import heapq

# 1st
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break

        if len(scoville) == 0:
            answer = -1
            break

        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2*min2
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer


## 2nd
import heapq


def solution(scoville, K):
    # help(heapq)

    cnt = 0
    heapq.heapify(scoville)
    # print(scoville)
    # 최소 숫자가 K를 넘어가면 배열 전체 숫자가 다 넘어감
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        # print(cnt)
        lowest_hot = heapq.heappop(scoville)
        second_hot = heapq.heappop(scoville)
        scoville_rate = lowest_hot + (2 * second_hot)
        heapq.heappush(scoville, scoville_rate)
        cnt += 1

    return cnt
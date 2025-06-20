import heapq 

def solution(jobs):

    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
            
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0] # 현재 시간으로부터 작업 소요시간 더하기
            answer += (now - cur[1]) # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1 # 처리한 후 작업 하나 증가
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
        
    return answer // len(jobs)
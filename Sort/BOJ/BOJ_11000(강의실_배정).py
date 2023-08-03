import heapq 

n = int(input())

arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append((s, t))
    # heapq.heappush(heap, (t, s))

arr.sort()

lecture_queue = []
heapq.heappush(lecture_queue, arr[0][1])

# print(heap)
start, end = 0, 0
for i in range(1, n):
    if arr[i][0] >= lecture_queue[0]:
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, arr[i][1])
    else:
        heapq.heappush(lecture_queue, arr[i][1])
    
    
print(len(lecture_queue))
        


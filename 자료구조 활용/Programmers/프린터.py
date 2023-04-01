from collections import deque

priorities = [2, 1, 3, 2]
# priorities = [1, 1, 9, 1, 1, 1]
location = 2
queue = []
for idx, elem in enumerate(priorities):
    queue.append((elem, idx))

queue = deque(queue)

cnt = 0
while queue:
    print(queue)
    max_val = max(queue, key=lambda x: x[0])[0]
    temp = queue.popleft()
    if temp[0] == max_val:
        cnt += 1
        if temp[1] == location:
            break
        pass
    else:
        queue.append(temp)

print(cnt)

'''
arr = [(0,10),(1,14),(2,2),(3,24)]
str = max(arr,key = lambda x:x[1]) 
'''

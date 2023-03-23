from collections import deque

# arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
answer = []
arr = deque(arr)

# for i in range(1, len(arr)+1):
#     if arr[i] == arr[i-1]:
#         arr.popleft()
n = len(arr)

while len(arr) > 1:
    idx = 0
    if arr[idx] == arr[idx+1]:
        arr.popleft()
    else:
        temp = arr.popleft()
        answer.append(temp)

answer.append(arr.popleft())

print(answer)
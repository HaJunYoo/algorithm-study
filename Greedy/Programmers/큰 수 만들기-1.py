from collections import deque

numbers = "98765"
k = 2
queue = deque(numbers)
stack = []
cnt = 0

stack.append(queue.popleft())

while queue and cnt<=k:
    print(stack)
    print(cnt)
    # 담으려는 것
    tmp = queue.popleft()
    while stack and stack[-1] < tmp and cnt<k:
        stack.pop()
        cnt+=1

    stack.append(tmp)


while cnt < k:
    stack.pop()
    cnt += 1
    print(stack)
    print(cnt)

stack += list(queue)


print(''.join(stack))






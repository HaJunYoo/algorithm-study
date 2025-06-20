from collections import deque

n, k = map(int, input().split())

queue = deque()

for i in range(1, n+1):
    queue.append(i)

while queue :
    # 1부터 k-1번째 원소까지 popleft를 한후 뒤에 append
    for i in range(1, k):
        num = queue.popleft()
        queue.append(num)
    # k 번째 원소는 그냥 버린다. => pop left
    queue.popleft()

    print(queue)

    if len(queue) == 1 :
        break

# 남은 원소 한개 출력
print(queue[0])
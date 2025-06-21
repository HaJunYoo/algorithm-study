
from collections import deque

n = int(input())

numbers = list()
for _ in range(n):
    numbers.append(list(map(int, input().split())))
ch = [[0] * n for _ in range(n)]

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

deq = deque()
sum = 0

deq.append((n // 2, n // 2))
ch[n // 2][n // 2] = 1
sum += numbers[n // 2][n // 2]
L = 0

def confirm(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

while True:
    if L == n // 2:
        break
    # while 문보다 for 문을 써야한다
    # 하나의 레벨에서 넣은 좌표들을 먼저 소모하고 그리고 난 후 다시 다음 레벨로 가야한다
    # while을 하게 되면 모든 원소를 다 탐색하게 된다
    for _ in range(len(deq)):
        x, y = deq.popleft()
        print(x, y)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if confirm(new_x, new_y):
                if ch[new_x][new_y] == 0:
                    sum += numbers[new_x][new_y]
                    ch[new_x][new_y] = 1
                    deq.append((new_x, new_y))

    print(L, len(deq))
    for x in ch:
        print(x)
    L += 1

'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
'''

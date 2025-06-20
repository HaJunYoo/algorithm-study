# # 원형 큐 문제
# n, k = map(int, input().split())
#
# numbers = [i for i in range(1, n+1)]
#
# tar_list = []
# idx = 0
# while numbers:
#     idx += k-1
#     if idx >= len(numbers):
#         idx %= len(numbers)
#     temp = numbers.pop(idx)
#     tar_list.append(str(temp))
# # print('<', end='')
# # print(str(tar_list)[1:-1], end='')
# # print('>')
# print("<",', '.join(tar_list),">", sep="")
from collections import deque

n, k = map(int, input().split())

numbers = [i for i in range(1, n+1)]
numbers = deque(numbers)

idx = k-1
tar_list = []
while numbers:
# print(numbers)
    for _ in range(idx):
        temp = numbers.popleft()
        numbers.append(temp)
    target = numbers.popleft()
    tar_list.append(str(target))


print("<",', '.join(tar_list),">", sep="")

'''
7 3
<3, 6, 2, 7, 5, 1, 4>
'''
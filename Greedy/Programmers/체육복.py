
n = 6
lost = [3, 4, 5]
reserve = [3, 4, 6]
########################

from collections import deque
student = []
for k in range(1, n + 1):
    student.append(k)

lost1 = set(lost)
reserve1 = set(reserve)
lost_set = lost1 - reserve1
reserve_set = reserve1 - lost1

lost = list(lost_set)
reserve = list(reserve_set)

print(lost)
print(reserve)
reserve = deque(reserve)

while reserve:
    temp = reserve.popleft()

    if temp-1 > 0 and temp-1 in lost:
        lost.remove(temp-1)

    elif temp+1 <= n and temp+1 in lost:
        lost.remove(temp+1)

    else:
        continue

print(lost)
print(student)
lost = deque(lost)
while lost:
    t1 = lost.popleft()
    if t1 in student:
        student.remove(t1)

print(student)
print(len(student))

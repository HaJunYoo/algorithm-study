from collections import deque

people = [70, 80, 50]
limit = 100

answer = 0
people.sort()
people = deque(people)
# print(people)

while people:
    w = 2
    temp = limit
    min_val = people[0]
    max_val = people[-1]

    if min_val + max_val <= limit and len(people) >= 2:
        people.popleft()
        people.pop()
        answer += 1
    else:
        people.pop()
        answer += 1


print(answer)
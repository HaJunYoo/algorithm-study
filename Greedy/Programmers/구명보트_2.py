from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)

    ans = 0
    while people:

        if len(people) == 1:
            ans += 1
            people.popleft()
            break

        if people[0] + people[-1] <= limit:
            people.popleft()

        people.pop()
        ans += 1

    return ans
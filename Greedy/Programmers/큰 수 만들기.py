from collections import deque

number = "4177252841"
k = 4

answer = []

for front in number:
    if not answer:
        answer.append(front)
        continue
    while answer[-1] < front and k > 0:
        answer.pop()
        k -= 1
        if not answer or k <= 0:
            break
    answer.append(front)
    if len(answer) == len(number) - k:
        break

print(''.join(answer))
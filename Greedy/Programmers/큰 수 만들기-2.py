from collections import deque


def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1

        # 숫자는 계속 stack에 누적시킴
        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
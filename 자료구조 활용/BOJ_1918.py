from collections import deque

S = input()

stack = list()
answer = ''

queue = deque(S)

while queue:
    elem = queue.popleft()
    print(answer)
    print(stack)
    if elem == '(':
        stack.append(elem)

    elif elem == '*' or elem == '/':
        while stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(elem)

    elif elem == '+' or elem == '-':
        while stack and (stack[-1] != '('):
            answer += stack.pop()
        stack.append(elem)

    elif elem == ')':
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.pop()

    elif elem.isalpha():
        answer += elem

while stack:
    answer += stack.pop()

print(answer)
# A+B*C-D/E
# A*(B+C)
# s = "(())()"
# s = ")()("
# s = "()()"
# s = "(())()"
s = "(()("

from collections import deque

# 스택을 만듦
# 만약 스택 마지막에 넣은 값이 큐의 처음값과 같지 않다면 answer flag True 유지
# 만약 위의 경우가 같다면 False
# 만약 큐의 처음 괄호가 ) 일 경우 False
# 큐에서 popleft한 값이 ( 일 경우는 True 유지
# 단, ( 였던 횟수만큼 )이 없으면 False

def solution(s):
    answer = True

    queue = deque(s)
    # print(queue)
    cnt = 0

    while queue:
        print(queue)
        print(answer)
        # print(cnt)
        if queue[0] == '(':
            queue.popleft()
            cnt += 1

        else:
            queue.popleft()
            cnt -= 1

        print(cnt)

        if cnt < 0:
            answer = False

    if cnt > 0:
        answer = False

    print(answer)
    return answer


solution(s)
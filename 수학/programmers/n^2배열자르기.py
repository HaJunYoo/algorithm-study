def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        x = i // n
        y = i % n
        elem = max(x, y) + 1
        answer.append(elem)
    return answer
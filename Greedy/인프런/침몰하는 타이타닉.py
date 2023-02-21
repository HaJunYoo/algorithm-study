from collections import deque

n, m = map(int, input().split())

weights = list(map(int, input().split()))

weights.sort()

weights = deque(weights)

cnt = 0
while len(weights) != 0:
    if len(weights) == 1:
        cnt += 1
        weights.pop()

    else :
        if weights[0] + weights[-1] > m :
            weights.pop()
            cnt += 1
            print(weights)

        else :
            weights.popleft()
            weights.pop()
            cnt += 1
            print(weights)

print(cnt)

'''
5 140
90 50 70 100 60
'''
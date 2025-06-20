'''
from collections import deque

n, m = map(int, input().split())
danger_list = list(map(int, input().split()))

danger = deque()

for idx, elem in enumerate(danger_list) :
    obj = (idx, elem)
    danger.append(obj)

print(danger)


# 순서는 0 부터 시작된다
cnt = 0

temp_max_val = 0

while danger :
    temp_max = sorted(danger, key=lambda x : x[1], reverse=True)[0]
    temp_max_val = temp_max[1]
    # print(temp_max_val)
    patient = danger.popleft()

    # print(patient)
    if patient[1] == temp_max_val :
        cnt += 1
        if patient[0] == m :
            break
    else :
        danger.append(patient)



print(cnt)

'''
from collections import deque

n, m = map(int, input().split())
Q = list(map(int, input().split()))

danger = deque()

cnt = 0

for idx, elem in enumerate(Q) :
    obj = (idx, elem)
    danger.append(obj)

while True :
    cur = danger.popleft()
    # 단 한개라도 아래 조건을 만족하는 참인 조건이 있다면 True를 반환
    if any(cur[1] < x[1] for x in danger) :
        danger.append(cur)

    else :
        cnt +=1
        if cur[0] == m :
            break

print(cnt)
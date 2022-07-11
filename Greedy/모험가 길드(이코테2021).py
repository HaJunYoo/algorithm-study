n = int(input())

people = list(map(int, input().split()))

people.sort()

# 변수를 2개 만든다.

# 그룹에 포함된 모험가의 수
count = 0
# 그룹
result = 0

for person in people : # 공포도를 낮은 것부터 확인
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= person : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹을 결성
        result += 1 # 그룹 수
        count = 0 # 현재 그룹에 포함된 모험가의 수는 초기화

print(result)


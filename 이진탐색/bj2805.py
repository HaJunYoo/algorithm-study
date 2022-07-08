n, m  = map(int, input().split())

trees = list(map(int, input().split()))

# 시작점과 끝점

start = 0
end = max(trees)

# 최소값 저장 변수
result = 0
# 이진 탐색 수행
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in trees :

        if x > mid :
            total += x - mid

    if total < m :
        end = mid-1

    else :
        result = mid
        start = mid+1


print(result)

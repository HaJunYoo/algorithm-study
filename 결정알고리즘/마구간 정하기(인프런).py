def Count(length):
    cnt = 1
    ep = horse[0]
    for i in range(1, n):
        if horse[i] - ep >= length :
            cnt+=1
            ep = horse[i]

    return cnt


n, c = map(int, input().split())

horse = []

for _ in range(n):
    horse.append(int(input()))

horse.sort()

# 재 배치 문제

lt = 0
rt = horse[-1]

res = 0

while lt <= rt :
    mid = (lt+rt)//2
    if Count(mid) >= c :
        res = mid
        lt = mid + 1
    else :
        rt = mid -1

print(res)
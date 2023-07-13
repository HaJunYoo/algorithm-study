n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d=[10001]*(m+1)

d[0]=0
# 동전 루프
for i in range(n):
    for j in range(array[i], m+1):
        # array[i] = k = 화폐 단위
        # i -> d 인덱스
        # 인덱스-동전금액 (i-k)원을 만드는 방법이 존재
        if d[j-array[i]] != 10001:
            # 
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
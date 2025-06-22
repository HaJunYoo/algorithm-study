n, m = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
cnt = 0
current_sum = 0

while True:
    # sum이 M보다 크면 start를 오른쪽으로 이동하여 합을 줄임
    if current_sum > m:
        current_sum -= arr[start]
        start += 1
    # end가 오른 쪽 끝인 n을 벗어나면 안됨
    elif end > n-1:
        break
    # sum이 M보다 작으면 end를 오른쪽으로 이동해서 합을 키움
    else:
        current_sum += arr[end]
        end += 1

    if current_sum == m:
        cnt += 1

print(cnt)
n = int(input())

meetings = []

# max_end = 0
for _ in range(n):
    # 시작, 끝
    a, b = map(int, input().split())
    meetings.append((a, b))
    # max_end = max(b, max_end)

# 끝 시간, 시작 시간 오름차순 정렬
meetings.sort(key= lambda x: (x[1], x[0]))

# print(meetings)
# print(max_end)

start_time, end_time = 0, 0

cnt = 0
for n_s, n_e in meetings:
    if end_time <= n_s:
        start_time = n_s
        end_time = n_e
        cnt += 1
        # print(f'{start_time} {end_time}')

print(cnt)
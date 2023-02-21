'''
# 내 풀이 => 시간 복잡도 O(n^2)
n = int(input())
s = []
new = []
for _ in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

s.sort(key=lambda x: (x[0], x[1]))
# print(s)

for i in range(n):
    # 키 몸무게 둘 다 작으면
    for j in range(i+1, n):
        # if i == j:
        #     continue

        if s[i][0] < s[j][0] and s[i][1] < s[j][1] :
            new.append(s[i])
            # print(s[i])
            break

# print(new)
print(len(s)-len(new))
'''

n = int(input())
s = []
new = []
for _ in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

s.sort(key=lambda x: -x[0])
# print(s)

max_val = 0
cnt = 0
for i in range(n):
    if s[i][1] > max_val:
        max_val = s[i][1]
        cnt += 1

print(cnt)
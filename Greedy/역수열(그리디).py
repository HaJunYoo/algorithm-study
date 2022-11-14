
n = int(input())

seq = list(map(int, input().split()))
# 5 3 4 0 2 1 1 0
# numbers = [num for num in range(1, n+1)]

v = []
# 뒤에서부터 숫자를 본다
# 8보다 큰 수 = 0
# 7보다 큰 수 = 1 -> 8, 7
# 6보다 큰 수 = 1 -> 8, 6, 7
# 5보다 큰 수 => 2 -> 8, 6, 5, 7

# O(n^2)
for i in range(n, 0, -1):
    # index = i-1
    # print(i)
    idx = seq[i - 1]
    v.insert(idx, i)
    # insert의 시간 복잡도 O(n)

for elem in v:
    print(elem, end=' ')




'''
8
5 3 4 0 2 1 1 0
'''
'''
n = int(input())
a = list(map(int, input().split()))
seq = [0]*n

for i in range(n):
    for j in range(n):
        # a[i] == 0 : 앞의 빈 공간 확보,
        # 해당 인덱스 비어있는지 seq[j] == 0
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=' ')


'''

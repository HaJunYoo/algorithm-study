place = input()

place_num = {'a' : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}

x, y = tuple(x for x in place)

# 행
x = place_num[x]
# 열
y = int(y)

print(x)
print(y)

# 동 서 남 북
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
cnt = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        # print(f'{nx}, {ny}')
        cnt += 1

print(cnt)
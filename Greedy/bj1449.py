N, L = map(int, input().split())

holes = list(map(int, input().split()))

pipe = [0 for _ in range(1001)]

for i in range(len(pipe)):
    if i in holes :
        pipe[i]+=1

x = 0
num = 0
while x < 1001 :
    if pipe[x] != 0 :
        num +=1
        x += L

    else :
        x+=1

print(num)

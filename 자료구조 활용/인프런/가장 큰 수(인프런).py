num, m = map(int, input().split())

# num의 리스트 화
num = list(map(int, str(num)))

# 스택을 통해 자기 앞에 자신보다 작은 수를 없앤다
stack = []

for x in num :
    while stack and m > 0 and stack[-1] < x :
        stack.pop()
        m -= 1

    stack.append(x)

if m!=0 :
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)
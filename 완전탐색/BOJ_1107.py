n = int(input())
m = int(input())
broken = [False] * 10 # 고장 여부

if m > 0:
    a = list(map(int, input().split()))
else:
    a = []

for x in a:
    broken[x] = True

def possible(c):

    if c == 0:
        if broken[0]: # 0 버튼이 고장났을 때
            return 0 # 이동 불가능
        else:
            return 1 # 이동할 수 있다 => 자리수는 1

    l = 0

    while c > 0:
        # c 10으로 나눈 나머지 숫자가 고장 버튼이면 0 리턴 아닐 시 자릿수 증가
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    # l : c의 숫자 개수 리턴
    return l

ans = abs(n-100) # 정답의 초기값

for i in range(0, 1000000+1):
    c = i
    l = possible(c) # 이동할 수 있는지 확인 후 이동 가능 시 자릿수 받음
    if l > 0:
        press = abs(c-n)
        if ans > l + press:
            ans = l + press

print(ans)
'''

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
'''

n, k = map(int, input().split())

# 26 -> 5 -> 1
cnt = 0
flag = True
while( n%k != 0 ) :
    n -= 1
    cnt += 1
    print(f'{n} : {cnt}')

while(flag) :
    print(f'{n} : {cnt}')
    n = n//k
    cnt += 1
    if n == 1 :
        print(f'{n} : {cnt}')
        flag = False

print(cnt)

################################################## 정답 문제풀이 ########

n, k = map(int, input().split())

result = 0

while True:
    # n 이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k

    # 마지막 n이 1일 때 0 을 빼서 1이 더해짐 => 반복문을 빠져나와서 1을 빼줘야함
    result += (n - target)

    n = target

    print(f'n :{n} result : {result} target : {target}')

    # n이 k보다 작을 때 반복문 탈출 -> 더 이상 나눌 수 없음
    if n < k:
        break

    # k로 나누기
    result += 1
    n //= k

    print(f'n :{n} result : {result} target : {target}')

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)

print(f'n :{n} result : {result} target : {target}')

print(result)
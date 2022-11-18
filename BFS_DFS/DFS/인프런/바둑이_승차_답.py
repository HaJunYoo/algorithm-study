# c : 무게 제한, n : n마리의 강아지
c, n = map(int, input().split())

# dog weight memoization
a = [0] * n

# 가장 작은 음수 선언
result = float("-inf")

for i in range(n):
    a[i] = int(input())

# 바둑이들의 무게 총합
total = sum(a)


def DFS(L, sum, tsum):
    # 함수 내부의 result와 외부 전역변수 result를 혼동하지 않게끔 선언 -> 전역변수 result를 사용할 것!
    global result

    # 추가 pruning -> 앞으로의 무게 적재 가능성이 최대값보다 작으면 탐색 종료
    if sum + (total - tsum) < result:
        return

    # 만약 sum이 무게 제한 c를 넘는다면 recurrsion stop
    if sum > c:
        return

    if L == n:
        if sum > result:
            result = sum
    else:
        # 참여 여부에 상관 없이 tsum에는 무게를 더한다.

        # 부분집합에 참여 시키겠다
        DFS(L + 1, sum + a[L], tsum + a[L])

        # 부분집합에 참여를 시키지 않겠다
        DFS(L + 1, sum, tsum + a[L])


# 0번째 인덱스부터 탐색 시작, sum = 0부터 시작
DFS(0, 0, 0)

# 제한을 넘지 않은 최대 무게 출력
print(result)
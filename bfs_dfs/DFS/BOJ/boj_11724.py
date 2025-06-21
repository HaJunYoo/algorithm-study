import sys

sys.setrecursionlimit(10 ** 6)
# 파이썬의 기본 recursive 한계는 1000인데 10의 6승으로 올린다

input = sys.stdin.readline
# 빠른 입력 함수
# 파이썬 내장 input은 조금 느리기 때문에 입력의 최대 호출이 많을 경우 시간 초과가 발생

N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    # index이기 때문에 1씩 줄여준다
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

# 연결요소 개수 변수
ans = 0
# 크기가 N개인 배열 생성
chk = [False] * N


# 들어오기 전에 체크를 해주는 방식을 더 추천
def dfs(now):
    for nxt in range(N):
        # now 노드에서 nxt 노드로의 간선이 있고 다음 노드를 방문 한 적이 없다면
        # 다음 노드 이동 전 chk[nxt]를 True해주고 dfs를 통해 다음 노드 방문
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    # 현재 방문한 노드의 chk[i]가 False(not True) 일 경우
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)  # dfs를 한번 호출하면 재귀형식으로 연결되어 있는 노드에 한해서 True를 찍어줄 것

print(ans)
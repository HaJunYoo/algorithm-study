# bfs 는 레벨 탐색을 하게 된다
# 큐 자료구조를 사용하게 된다
# 방문 여부를 확인하는 리스트와 트리의 깊이를 설정하는 리스트가 필요

from collections import deque

MAX = 10000
dis = [0] * (MAX+1)
ch = [0] * (MAX+1)

s, e = map(int, input().split())

ch[s] = 1
dis[s] = 0

queue = deque()
queue.append(s)

def confirm(coord):
    if coord < 1 or coord > 10000:
        return False
    else:
        return True


def bfs():
    global cnt

    while queue:
        now = queue.popleft()
        if now == e:
            break

        for next in (now-1, now+1, now+5):
            if confirm(next):
                if ch[next] == 0:
                    queue.append(next)
                    ch[next] = 1
                    dis[next] = dis[now]+1

bfs()
print(dis[e])
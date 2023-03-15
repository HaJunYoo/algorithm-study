res = 0

def dfs(energy, cnt, min_e_val, dungeons, visited):
    global res

    res = max(cnt, res)

    if cnt == len(dungeons):
        return

    # 이부분이 정답에 영향을 미치지 않지만 시간 복잡도는 줄여준다
    if energy < min_e_val:
        return

    for idx, dungeon in enumerate(dungeons):
        if not visited[idx]:
            min_e = dungeon[0]
            use_e = dungeon[1]

            if energy >= min_e:
                visited[idx] = True
                dfs(energy - use_e, cnt + 1, min_e_val, dungeons, visited)
                visited[idx] = False

            else:
                continue

def solution(k, dungeons):
    global res

    n = len(dungeons)

    min_e_list = [d[0] for d in dungeons]

    min_e_val = min(min_e_list)

    visited = [False] * n

    dfs(k, 0, min_e_val, dungeons, visited)

    print(res)

    return res





n, m = map(int, input().split())

problems = [tuple(map(int,input().split())) for _ in range(n)]

max_score = -237778

def dfs(cnt, score, time):
    global max_score

    pro = problems[cnt]

    if time > m:
        return

    # print(cnt)
    if cnt == n-1:
        if max_score < score:
            max_score = score
        return


    dfs(cnt+1, score+pro[0], time+pro[1])
    dfs(cnt+1, score, time)



dfs(0, 0, 0)
print(max_score)

"""
5 20
10 5
25 12
15 8
6 3
7 4
"""

# for idx, pro in enumerate(problems):
#     if not visited[idx]:
#         if time + pro[1] < m:
#
#             visited[idx] = True
#             score += pro[0]
#             time += pro[1]
#             numbers.append(idx)
#             dfs(cnt+1)
#             numbers.pop()
#             score -= pro[0]
#             time -= pro[1]
#             visited[idx] = False
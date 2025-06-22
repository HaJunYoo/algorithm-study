n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def check_paper(li, lj, ri, rj):

    if ri - li == 1 and rj - lj == 1:
        if graph[li][lj] == 1:
            return [0, 1]
        else:
            return [1, 0]

    first_value = graph[li][lj]
    is_consistent = True

    for i in range(li, ri):
        for j in range(lj, rj):
            if first_value != graph[i][j]:
                is_consistent = False
                break
        if not is_consistent:
            break

    if is_consistent:
        if first_value == 0:
            return [1, 0]
        else:
            return [0, 1]

    mi = (li + ri) // 2
    mj = (lj + rj) // 2

    res = [0, 0]
    rec0 = check_paper(li,lj,mi,mj)
    rec1 = check_paper(li,mj,mi,rj)
    rec2 = check_paper(mi,lj,ri,mj)
    rec3 = check_paper(mi,mj,ri,rj)

    res[0] = rec0[0] + rec1[0] + rec2[0] + rec3[0]
    res[1] = rec0[1] + rec1[1] + rec2[1] + rec3[1]
    return res


res = check_paper(0,0,n,n)
for ele in res:
    print(ele)
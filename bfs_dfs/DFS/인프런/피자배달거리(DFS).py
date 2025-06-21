def DFS(L, s):
    global res
    # 조합이 완성되었을 때
    if L==m:
        sum = 0
        # 치킨집 조합별 각 집의 피자 배달거리
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = x[0]
                y2 = x[1]
                dis = min(dis, abs(x1-x2)-abs(y1-y2))
            sum += dis
        if sum < res:
            res=sum

    else:
        for i in range(s, len(pz)):
            cb[L]=pz[i]
            DFS(L+1, i+1)




if __name__ =='__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split()))]
    hs = [] # 집을 담는 리스트
    pz = [] # 치킨집을 담는 리스트
    cb = [0]*m # 조합을 담는 리스트
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                hs.append((i, j))
            elif graph[i][j] == 2:
                pz.append((i, j))

    DFS(0, 0)
    print(res)

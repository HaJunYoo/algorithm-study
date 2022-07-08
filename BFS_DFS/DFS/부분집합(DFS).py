n = int(input())

ch = [0]*(n+1)

def DFS(v):
    if v == n+1 :
        for idx, elem in enumerate(ch) :
            if elem != 0 :
                print(idx, end = ' ')
        print()

    else :
        ch[v] = 1 # 사용한다
        DFS(v+1)
        ch[v] = 0 # 시용하지 않는다
        DFS(v+1) # 오


DFS(1)


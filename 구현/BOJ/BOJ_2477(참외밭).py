
if __name__ == '__main__':
    
    k = int(input())
    
    width = []
    height = []
    total = []
    for _ in range(6):
        dir, length = map(int, input().split())
        total.append(length)
        
        if dir == 1 or dir == 2:
            width.append(length)
        else:
            height.append(length)
    
    bigbox = max(height) * max(width)
    
    # 동 서 남 북
    dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    #세로 최대값 
    maxh_idx = total.index(max(height))
    #가로 최대값 
    maxw_idx = total.index(max(width))

    #전체 이동에서 세로 최대값의 다음값에서 세로 최대값 이전의 가로값을 빼준것이 작은 사각형의 가로값 
    small_h = abs(total[maxh_idx-1] - total[(maxh_idx-5 if maxh_idx == 5 else maxh_idx +1)])
    
    small_w = abs(total[maxw_idx-1] - total[(maxw_idx-5 if maxw_idx == 5 else maxw_idx +1)])

    area = bigbox - (small_h * small_w)

    print(area*k)
    

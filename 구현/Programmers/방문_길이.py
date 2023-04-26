if __name__ == '__main__':
    dirs = "LULLLLLLU"

    x, y = 0, 0  # 시작 좌표를 0, 0으로 지정
    map = dict()  # 좌표를 키로 사용하는 해시 생성 => (현재 좌표, 이동할 좌표)
    for command in dirs:  # O(dirs)
        if command == 'U' and y < 5:  # 위로
            map[(x, y, x, y + 1)] = True  # 현재 좌표, 이동할 좌표 -> 키
            # x, y 좌표 작은게 왼쪽으로~
            y += 1
        elif command == 'D' and y > -5:  # 아래로
            map[(x, y - 1, x, y)] = True  # 이동할 좌표, 현재 좌표
            y -= 1
        elif command == 'R' and x < 5:  # 오른쪽으로
            map[(x, y, x + 1, y)] = True  # 현재 좌표, 이동할 좌표
            x += 1
        elif command == 'L' and x > -5:  # 왼쪽으로
            map[(x - 1, y, x, y)] = True  # 이동할 좌표, 현재 좌표.
            x -= 1

    print(len(map))  # 추가된 값들이 곧 방문 길이
    print(map) # ss
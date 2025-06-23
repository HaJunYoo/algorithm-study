n = int(input())

layer = 1      # 현재 층 수 (1층부터 시작)
max_room = 1   # 현재 층의 최대 방 번호

while n > max_room:
    max_room += 6 * layer
    layer += 1

print(layer)
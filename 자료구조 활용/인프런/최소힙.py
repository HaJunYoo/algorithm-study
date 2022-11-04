from heapq import heappush, heappop

heap = list()

# heappush의 시간 복잡 o(log(n))
# heappop의 시간 복잡도 o(log(n)) -> min heap 자료구조를 유지하는데 시간복잡도 소요
def decide(x):
    global flag

    if x == 0:
        if len(heap) != 0:
            temp = heappop(heap) # 루트 노드 pop
            print(temp)
        else:
            print(-1)

    elif x == -1:
        flag = False

    else :
        heappush(heap, x)

flag = True

while flag:
    num = int(input())
    decide(num)


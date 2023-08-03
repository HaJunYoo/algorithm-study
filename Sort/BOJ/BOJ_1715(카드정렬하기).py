import heapq

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

heapq.heapify(cards)

res = 0
# print(cards)

if len(cards) >= 2:
    while cards:
        temp = []
        # print(cards)
        for _ in range(2):
            temp.append(heapq.heappop(cards))
        
        temp_sum = sum(temp)
        res += temp_sum
        if cards:
            heapq.heappush(cards, temp_sum)
            
# else:    
#     res += 0

print(res)
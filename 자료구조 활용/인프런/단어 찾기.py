# from heapq import heappush,heappop
#
# heap = []
#
# numbers, k = map(int, input().split())
#
# numbers = str(numbers)
#
# for num in numbers :
#     heappush(heap, int(num))
#
# for _ in range(k):
#     heappop(heap)
#
# print(numbers)

'''
n = int(input())

vocab = [input() for _ in range(n)]
poem = [input() for _ in range(n-1)]

word = set(vocab) - set(poem)
word = list(word)
print(word[0])

'''

n = int(input())

vocab = dict()

for _ in range(n):
    tmp1 = input()
    vocab[tmp1] = 1

for _ in range(n-1):
    tmp2 = input()
    vocab[tmp2] = 0

for key, val in vocab.items():
    if vocab[key] == 1 :
        print(key)
    break






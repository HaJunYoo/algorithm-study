n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
checks = list(map(int, input().split()))

cards_dict = {}

for e in cards:
    if cards_dict.get(e):
        cards_dict[e] += 1
    else:
        cards_dict[e] = 1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            # print(mid)
            # print(cards[mid])
            # print('---')
            return cards_dict[target]
    return 0


results = [binary_search(cards, check) for check in checks]
# print()
# print(cards)
print(' '.join(map(str, results)))

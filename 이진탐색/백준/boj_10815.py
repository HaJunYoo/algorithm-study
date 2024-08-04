# 해시 기반 풀이

n = input()

n_list = list(map(int, input().split()))

n_dict = dict()

for e in n_list:
    n_dict[e] = 1

m = input()

m_list = list(map(int, input().split()))

for i in m_list:
    if n_dict.get(i):
        print(1, end=" ")
    else:
        print(0, end=" ")

# ----
# 이분탐색
n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
checks = list(map(int, input().split()))


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return 1
    return 0


results = [binary_search(cards, check) for check in checks]
print(' '.join(map(str, results)))

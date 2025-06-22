from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)

m = int(input())
queries = list(map(int, input().split()))

def is_in_array(query) -> int:

    x = bisect_left(arr, query)

    if 0 <= x < len(arr) and arr[x] == query:
        return 1
    else:
        return 0


for q in queries:
    ans = is_in_array(query=q)
    print(ans)
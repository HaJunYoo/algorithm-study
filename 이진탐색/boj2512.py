
N = int(input())

citys = list(map(int, input().split()))

M = int(input())

lo = 0
hi = max(citys)
mid = (lo+hi)//2

ans = 0

def is_possible(x):
    return sum(min(city, x) for city in citys) <= M


while lo <= hi :
    if is_possible(mid):
        lo = mid+1
        ans = mid
    else :
        hi = mid-1

    mid = (lo+hi) // 2

print(ans)

# print(u_limit)

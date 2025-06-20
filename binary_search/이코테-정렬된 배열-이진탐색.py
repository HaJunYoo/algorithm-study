from bisect import bisect_left, bisect_right

# 값이 left value, right value인 데이터의 개수를 반환하는 함수
def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x, x] 범위 안에 있는 데이터의 수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않을 경우
if count == 0 :
    print(-1)

# 값이 존재할 경우
else :
    print(count)


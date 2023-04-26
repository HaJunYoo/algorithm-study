# 최솟값과 최대값을 찾아 반환
def find_max_min(array):
    max_val = -10000000
    min_val = 21800000
    for num in array:
        if num > max_val:
            max_val = num

        if num < min_val:
            min_val = num

    return min_val, max_val


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        t = int(input())
        num_list = list(map(int, input().split()))
        min_val, max_val = find_max_min(num_list)
        print(f'{min_val} {max_val}')

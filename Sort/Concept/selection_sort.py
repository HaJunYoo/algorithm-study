n = int(input())

arr = list(map(int, input().split()))

def selection_sort():
    for i in range(n-1):
        min_index = i
        for k in range(i+1, n):
            if arr[k] < arr[min_index]:
                min_index = k
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp

    return arr

selection_sort()

for elem in arr :
    print(elem, end= ' ')
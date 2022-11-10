n = int(input())

numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

m = int(input())

i = 0
j = -1

while (m != 0):
    # i보다 다음 인덱스가 더 커지면 다시 리스트 재정렬
    if numbers[i] < numbers[i+1] or numbers[j] > numbers[j-1]:
        numbers.sort(reverse=True)

    numbers[i] -= 1
    numbers[j] += 1

    m -= 1

print(max(numbers) - min(numbers))


'''
10
69 42 68 76 40 87 14 65 76 81
50
'''
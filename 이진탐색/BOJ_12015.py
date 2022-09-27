n = int(input())

numbers = list(map(int, input().split()))

array = []

numbers.sort()
print(numbers)

array.append(numbers[0])

# for i in range(1,len(numbers)+1) :
#     if
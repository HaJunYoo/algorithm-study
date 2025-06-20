# n = int(input())

MAX = 1000000

numbers = [x for x in range(2, MAX + 1)]

ch = [False] * (MAX + 1)

ch[0] = ch[1] = True

for num in numbers:
    if not ch[num]:
        temp = num + num
        for j in range(temp, MAX + 1, num):
            ch[j] = True


# print(ch)
def boolean(n):
    a, b = 0, 0
    ans = 0

    for i in range(n - 1, 1, -1):
        # 소수라면
        if not ch[i]:
            temp = n - i
            if temp > i:
                continue
            if not ch[temp]:
                b = i
                a = temp
                break


    if a == 0 and b == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f'{n} = {a} + {b}')


inputs = list()
# Flag = True

while True:
    temp_num = int(input())
    if temp_num == 0:
        break

    inputs.append(temp_num)

for n in inputs:
    boolean(n)


'''
예제 입력 1 복사
8
20
42
0

예제 출력 1 복사
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
'''
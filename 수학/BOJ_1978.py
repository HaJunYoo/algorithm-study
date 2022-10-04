def boolean(num):

    if num > 1 :

        div = num - 1

        while div > 1:

            if num % div == 0:
                return False

            else:
                div -= 1

        return True

    else :
        return False


n = int(input())

numbers = list(map(int, input().split()))

cnt = 0
for num in numbers:
    if boolean(num):
        cnt += 1

print(cnt)
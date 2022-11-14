
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0

string = ''
temp = []

while lt <= rt:
    if a[lt] > last:
        temp.append((a[lt], 'L'))
    if a[rt] > last:
        temp.append((a[rt], 'R'))

    temp.sort()

    # 이 부분 질문
    if len(temp) == 0:
        break

    else:
        last = temp[0][0]
        # print(last)
        tmp = temp[0][1]
        string += tmp

        if tmp == "L":
            lt += 1

        else:
            rt -= 1

    temp.clear()

print(string)
print(len(string))

'''
10
3 2 10 1 5 4 7 8 9 6
'''

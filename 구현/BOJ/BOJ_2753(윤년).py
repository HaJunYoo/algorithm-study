if __name__ == '__main__':
    year = int(input())

    flag = False
    res = 0
    if year % 400 == 0:
        flag = True
    elif year % 100 != 0 and year % 4 == 0:
        flag = True
    else:
        flag = False

    if flag:
        res = 1
    else:
        res = 0

    print(res)
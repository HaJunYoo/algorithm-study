def decimal_to_bin(n):
    if n == 1:
        return str(1)

    mok = n // 2

    output = decimal_to_bin(mok)

    cur = n % 2

    return output + str(cur)



if __name__ == '__main__':
    n = int(input())
    print(decimal_to_bin(n))
# n = int(input())
#
# string = ""
#
#
# for i in range(1, n+1):
#     string += str(i)
#
# print(len(string))

n = int(input())

start = 1

end = 1

length = 1

ans = 0

# 자리수가 바뀌는 10, 100 또한 생각해야한다
# 반드시 이하를 써줘야한다
while (start <= n) :

    end = (start * 10) - 1

    if end > n :
        end = n

    temp = length * (end - start + 1)

    ans += temp

    # start를 다음 자리수로 이동
    # length(자리수)를 1 증가
    start = end + 1
    length += 1

print(ans)
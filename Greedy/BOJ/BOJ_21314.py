import math
def solution(data):
    max = "" #최댓값 결과
    min = "" #최솟값 결과
    m = 0

    for i in range(len(data)):
        if data[i] == 'M':
            m += 1 #M이 나온다면 m을 증가
        elif data[i] == 'K':
            if m: #M후에 K가 연속해서 나온 경우라면
                min += str(pow(10,m) + 5) #최솟값의 경우 5를 더해주고
                max += str(5 * pow(10,m)) #최댓값의 경우 5를 곱해준다
            else: #만일 이전에 M 등장 없이 K만 두번 이상 연속된 경우
                min += "5" 
                max += "5"
            m = 0
    if m > 0: #'K'없이 'M'들로 문자열이 끝난 경우
        min += str(10 ** (m-1))
        while m:
            max += "1"
            m -= 1
    print(max)
    print(min)

if __name__ == '__main__':
    mks = input()  #   민겸수 받아옴

    solution(mks)
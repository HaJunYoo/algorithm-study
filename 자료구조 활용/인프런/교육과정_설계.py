from collections import deque

string = input()
n = int(input())

essential_list = [s for s in string]

plans = [input() for _ in range(n)]

# essential의 0번째 인덱스에 해당할 경우 essential을 pop left

for idx, plan in enumerate(plans) :
    # 루프 안에서 디큐를 새로 생성해주어야 한다.
    essential = deque(essential_list)
    # print(plan)
    for edu in plan :
        try :
            first = essential[0]
            # print(first)
            if edu == first:
                essential.popleft()
        except : pass


    if len(essential) != 0 :
        print(f'#{idx+1} NO')
    else :
        print(f'#{idx + 1} YES')

'''
MNBVCX
10
QWEMRNTBYVUASDFGCX
RTYMUNIBOVACSXDQFWE
DFGMKNJBLAVQCWXE
RKJHDGAFQZWXECRVTBY
QWERTYUMNBVASDFGCXAJK
MPNBVCXZSAOFIGUHYJTKREW
MQNBVUCXE
NKJHDGAFQZWXECRVTBY
OQASWDFEGRHTCJVYK
QMTNBOVFDCGXP

#1 YES
#2 YES
#3 YES
#4 NO
#5 YES
#6 YES
#7 YES
#8 NO
#9 NO
#10 YES
----------
POIUYTREW
9
ASDPFOGIHJUKYZTXRCEVWBNM
QASWDFEGRHTCJVYK
PBOVICXZSDUAYFTGRHEJWKL
KJHDGAFQZWXECRVTBY
WOPASFKGHDEF
MPNBVCXZSAOFIGUHYJTKREW
MZCTSBDEA
NKJHDGAFQZWXECRVTBY
OQASWDFEGRHTCJVYK

#1 YES
#2 NO
#3 YES
#4 NO
#5 NO
#6 YES
#7 NO
#8 NO
#9 NO
'''
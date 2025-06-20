def solution(numbers, hand):
    location = { 
            1: (0,0), 2:(0,1), 3:(0,2),
            4: (1,0), 5:(1,1), 6:(1,2),
            7: (2,0), 8:(2,1), 9:(2,2),
            '*':(3,0), 0:(3,1), '#':(3,2)
            }
    
    num_hand = { 
            1: 'L', 2:'C', 3:'R',
            4: 'L', 5:'C', 6:'R',
            7: 'L', 8:'C', 9:'R',
            '*':'L', 0:'C', '#':'R'
            }


    def get_center_hand(c_target, r_hand, l_hand):
        x1, y1 = location[c_target]
        x2, y2 = r_hand
        x3, y3 = l_hand
        
        r_dis = abs(x1 - x2) + abs(y1 - y2)
        l_dis = abs(x1 - x3) + abs(y1 - y3)
        
        if r_dis == l_dis:
            if hand == "right":
                return 'R'
            else:
                return 'L'
        else:
            if r_dis < l_dis:
                return 'R'
            else:
                return 'L'


    left_index = location['*']
    right_index = location['#']

    answer = ''
    for num in numbers:
        coord = location[num]
        # print(coord)
        
        required_hand = num_hand[num]
        
        char = ''
        if required_hand == 'C':
            char = get_center_hand(num, right_index, left_index)
        else:
            char = required_hand
        
        answer += char
        
        if char == 'R':
            right_index = coord
        else:
            left_index = coord
        
    return answer
            

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    result = "LLRLLRLLRL"
    answer = solution(numbers, hand)
    print(answer)
    if answer == result:
        print('정답')
    else:
        print('오답')
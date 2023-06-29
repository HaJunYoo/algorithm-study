def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha == ' ': 
            answer += alpha
            continue
        else:
            corr = ord('a') if alpha.islower() else ord('A')
            
            alpha = chr( (ord(alpha) - corr + n) % 26 + corr ) 
            # print(alpha)
            answer += alpha
    
    print(answer)
    return answer
    
if __name__ == '__main__':
    s = "a B z"	
    n = 4
    solution(s, n)
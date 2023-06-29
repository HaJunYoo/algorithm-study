def solution(s:str) -> str:
    answer = ''
    
    n = len(s)
    
    cnt = 0
    for idx in range(n):
        
        if s[idx] == ' ':
            answer += s[idx]
            cnt = 0
            continue
        
        if cnt % 2 == 0:
            answer += s[idx].upper()
        else:
            answer += s[idx].lower()
        cnt += 1
        
        
    return answer
    
    
    
    
if __name__ == '__main__':
    s = "try hello world"
    answer = solution(s)
    print(answer)
from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    
    q = deque()
    q.append([begin, 0])
    visited = [0]*len(words)
    while q:
        word, count = q.popleft()
        if word == target : return count
    
        for i in range(len(words)):
            if visited[i] == 0:
                diff_arr = [x!=y for x, y in zip(word, words[i])]
                diff = sum(diff_arr)
                if diff == 1:
                    q.append([words[i], count+1])
                    visited[i] = 1
                else: continue
            else: continue
                
    return 0
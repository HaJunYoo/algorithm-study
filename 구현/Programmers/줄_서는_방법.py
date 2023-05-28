from itertools import permutations

def solution(n, k):
    answer = []
    for idx, permute in enumerate(permutations(range(1,n+1), n), 1):
        if idx == k:
            answer = list(permute)
    
    
    return answer
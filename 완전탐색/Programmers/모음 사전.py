## 풀이 1

from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1


### 풀이 2

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1

# ### 풀이 3


def solution(word):
    words = []
    alphabet = ['A', 'E', 'I', 'O', 'U']

    def dfs(step, string):
        if step == 5:
            return

        for w in alphabet:
            next_string = w + string
            words.append(next_string)
            dfs(step + 1, next_string)
            # words.pop()

    dfs(0, '')
    # print(words)
    words.sort()
    # print(words)

    return words.index(word) + 1
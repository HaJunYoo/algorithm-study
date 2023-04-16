from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = deque(skill)
        for s in skill_tree:
            print(skill_list)

            if s in skill and s != skill_list.popleft():
                break
        else:  # for-else 문법을 사용하면 dirty flag를 제거할 수 있고 파이썬스럽게 푼 느낌이 든다.
            answer += 1
    print(answer)
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)
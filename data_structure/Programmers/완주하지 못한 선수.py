participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    # answer = ''
    member = dict()
    participant_list = list(set(participant))
    n_completion = list()

    for part in participant_list:
        member[part] = 0

    for p in participant:
        member[p] += 1

    for c in completion:
        if member[c] > 0:
            member[c] -= 1

    answer = ''
    for m, v in member.items():
        if v > 0:
            answer += m

    print(answer)
    return answer


solution(participant, completion)